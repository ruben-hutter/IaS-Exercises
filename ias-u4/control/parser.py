from protocol import Protocol
from sender import Sender

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
			line = config.readline()
			# reached eof
			if not line:
				# send finale to last peer
				if peer_id:
					Sender.send_msg(peer_id, Protocol.FINALE)
				config.close()
				return
			line = line.rstrip()
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