# control node code goes here
import socket

class Controller:
	# update the networks topology according to the passed config file
	@staticmethod
	def topology_update(config_file):
		# read config and update peers
		Parser.parse_file(config_file)

# protocol message prefixes
class Protocol:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'
	FINALE = 'FIN'

# cli command prefixes
class Commands:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'

# parser to parse input files
class Parser:
	# send links and peer addresses to specified peer
	@staticmethod
	def send_topology_update(peer_id, peer_links):
		message = Protocol.TOPOLOGY_UPDATE+':'
		# append node id
		message.append(peer_id)
		# send names of nodes
		for peer_name in Sender.peer_addresses.keys():
			message.append(' ' + peer_name)
		message.append(':')
		# send ip addr of links
		for peer in peer_links.split(',').split(' ')[0]:
			message.append(' '.join('_'.join([peer, Sender.get_peer(peer[0]), Sender.get_peer(peer[1])])))
		message.append(':')
		# send links
		message.append(peer_links)
		# send message to peer
		Sender.send_msg(peer_id, message)

	# parse the config file
	@staticmethod
	def parse_file(file):
		# open file
		config = open(file)
		# read lines and parse topology info
		peer_id = ''
		while True:
			line = file.readline()
			# reached eof
			if not line:
				# send finale to last peer
				if peer_id:
					Sender.send_msg(peer_id, Protocol.FINALE)
				config.close()
				return
			# line is node declaration
			if line.startswith('addr'):
				# split line
				line = line.split(':')
				# get id
				peer_id = line[0][4:]
				# get addr
				peer_addr = line[1]
				# get port
				peer_port = line[2]
				# write addr to dict
				Sender.add_peer(peer_id, peer_addr, peer_port)
				continue
			# line is link declaration
			if line.startswith('link'):
				# split line
				line = line.split(':')
				# get id
				peer_id = line[0][4:]
				# get links
				peer_links = line[1]
				send_topology_update(peer_id, peer_links)

# sends messages over tcp
class Sender:
	peer_addresses = {}

	# return a peers address
	@staticmethod
	def get_peer(peer_id):
		return peer_addresses[peer_id]

	# adds a peer to the peer list
	@staticmethod
	def add_peer(peer_id, peer_addr, peer_port):
		peer_addresses[peer_id] = (peer_addr,peer_port)

	# sed message to address
	@staticmethod
	def send_msg(peer_id, msg):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(peer_addresses[peer_id])
			sock.send(msg.encode())
			sock.close()
			print(f'> {peer_id}@{str(peer_addresses[peer_id])}: {msg}')
		except:
			print(f"> ERROR: Couldn't connect to {peer_id}@{str(peer_addresses[peer_id])}!")

# cli for user input
class Cli:
	# run the cli
	@staticmethod
	def run():
		while True:
			cmd = input('Enter command: ')
			if cmd.startswith(Commands.MESSAGE):
				tokens = cmd.split(' ')[1:]
				if len(tokens) < 3:
					print(f'> Invalid args! Usage: {Protocol.MESSAGE} <sender:id> <receiver_id> <message>')
					continue
				message = Protocol.MESSAGE + ':'.join(tokens[:2]) + ':' + ' '.join(tokens[2:])
				Sender.send_msg(tokens[0], message)
				continue
			if cmd.startswith(Commands.TOPOLOGY_UPDATE):
				if len(tokens) != 2:
					print(f'> Invalid args! Usage: {Protocol.TOPOLOGY_UPDATE} <config_file>')
					continue
				Controller.topology_update()
				return
