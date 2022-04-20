# control node code goes here
import socket

class Controller:
	# update the networks topology according to the passed config file
	def topology_update(config_file):
		# read config and update peers
		parser.parse_file(confilg_file, sender)

# protocol message prefixes
class Protocol:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'

# cli command prefixes
class Commands:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'

# parser to parse input files
class Parser:
	# parse the config file
	def parse_file(file, sender):
		# open file
		config = open(file)
		# read lines and parse topology info
		for line in config:
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
				sender.add_peer(peer_id, peer_addr, peer_port)
				continue
			# line is link declaration
			if line.startswith('link'):
				# split line
				line = line.split(':')
				# get id
				peer_id = line[0][4:]
				# get links
				peer_links = line[1]
				send_links(peer_id, peer_links, sender)
				continue

	# send links and peer addresses to specified peer
	def send_links(peer_id, peer_links, sender):
		message = [Protocol.TOPOLOGY_UPDATE]
		for link in peer_links.split(','):
			message.append(sender.get_peer(link.split(' ')[1]))
			message.append(link)
		message = ' '.join(message)
		Sender.send_msg(peer_id, message)

# sends messages over tcp
class Sender:
	peer_addresses = {}

	# return a peers address
	def get_peer(peer_id):
		return peer_addresses[peer_id]

	# adds a peer to the peer list
	def add_peer(peer_id, peer_addr, peer_port):
		peer_addresses[peer_id] = (peer_addr,peer_port)

	# sed message to address
	def send_msg(peer_id, msg):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(peer_addr[peer_id])
			sock.send(msg)
			sock.close()
			print(f'> {peer_id}@{str(peer_addr[peer_id])}: {msg}')
		except:
			print(f"> ERROR: Couldn't connect to {peer_id}@{str(peer_addr[peer_id])}!")

# cli for user input
class Cli:
	# run the cli
	def run():
		while True:
			cmd = input('Enter command: ')
			prefix = cmd.split(' ')[0]
			tokens = cmd.split(' ')[1:]
			if prefix == Command.MESSAGE:
				if len(tokens) < 4:
					print(f'> Invalid args! Usage: {Protocol.MESSAGE} <sender:id> <receiver_id> <message>')
					continue
				message = Protocol.MESSAGE + ' ' + ' '.join(tokens[1:])
				Sender.send_msg(tokens[0], message)
				continue
			if prefix == Command.TOPOLOGY_UPDATE:
				if len(tokens) != 2:
					print(f'> Invalid args! Usage: {Protocol.TOPOLOGY_UPDATE} <config_file>')
					continue
				Controller.topology_update()
				return
