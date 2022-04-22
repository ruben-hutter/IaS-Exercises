from protocol import Protocol
import sender

# parser to parse input files
# send links and peer addresses to specified peer
def send_topology_update(peer_id, peer_links):
	message = Protocol.TOPOLOGY_UPDATE+':'
	# append node id
	message += peer_id
	# send names of nodes
	for peer_name in sender.peer_addresses.keys():
		message += (' ' + peer_name)
	message += ':'
	# send ip addr of links
	for peer_link in peer_links.split(','):
		peer = peer_link.split(' ')[0]
		message += (' '.join('_'.join([peer, sender.get_peer(peer)[0], sender.get_peer(peer)[1]])))
	message += ':'
	# send links
	message += peer_links
	# send message to peer
	sender.send_msg(peer_id, message)

# parse the config file
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
				sender.send_msg(peer_id, Protocol.FINALE)
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
			send_topology_update(peer_id, peer_links)
