# peer node code goes here...
import socket

# launch node
def launch(ip_addr, port):
	# create server socket to bind incomin connections
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip_addr, port))
	sock.listen()
	print(f'Peer listening on {ip_addr}:{port}')
	# wait for incoming connections
	while True:
		# accept connection from othe peer
		peer_sock, peer_addr = sock.accept()
		try:
			# receive message from other peer
			msg = connection.recv()
			if msg:
				parse_input(msg)
			else:
				break
		finally:
			# close connection when finished
			peer_sock.close()

# parse messages received from peer
def parse_input(message):
	message = message.decode()
	if message.startswith(Protocol.TOPOLOGY_UPDATE):
		parse_ntu(message.split(':'))
		return
	if message.startswith(Protocol.MESSAGE):
		parse_message(message.split(':'))
		return

# run ntu
def parse_ntu(ntu_tokens):
	# process peer names
	names = ntu_tokens[0].split()
	for name in names:
		# empty string
		if not name or not name.strip():
			continue
		Routing.add_route(name)
	# process peer addresses
	addrs = ntu_tokens[1].split()
	for addr in addrs:
		# empty string
		if not addr or not addr.strip():
			continue
		addr_tokens = addr.split('_')
		# add peer addr to peer addersses
		peer_addr[addr_tokens[0]] = (addr_tokens[1],int(addr_tokens[2]))
	# process peer links
	links = ntu_tokens[2]
	for link in links.split(','):
		# empty string
		if not link or not link.strip():
			continue
		dest_id  = link.split(',')[0]
		rtt = link.split(',')[1]
		Routing.set_rtt(dest_id, rtt)

# process message
def parse_msg(message_tokens):
	if message_tokens[2] == node_id:
		msg = ' '.join(message_tokens[3:]
		print(f'Message received from node {message_tokens[1]}:')
		print(msg)
		return
	message_tokens[1] = node_id
	forward_msg(':'.join(message_tokens))

# protocol message prefixes
class Protocol:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'

# stores the routing table
class Routing:

	INFINITE = -1
	NO_HOP = ''

	node_id = ''
	peer_addr = {}
	routing_table = {}

	# add entry to routing table
	def add_route(dest_id):
		routing_table[dest_id] = [INFINITE, NO_HOP]

	# returns the RTT to destination
	# returns Routing.INFINITE  if no route found
	def get_rtt(dest_id):
		return routing_table[dest_id][0]

	# set rtt to destination
	def set_rtt(dest_id, rtt):
		routing_table[dest_id][0] = rtt

	# return next hop to destination
	# return ROUTING.NO_HOP  if no route found
	def get_next_hop(dest_id):
		return routing_table[dest_id][1]

	# set next hop to destination
	def set_next_hop(dest_id, next_hop_id):
		routing_table[dest_id][1] = next_hop_id

''' 	# update of least cost from x to y
	def update_dist(rcv_id, rcv_vec):
		for i in range(1,len(forwarding_table)):
			if i == rcv_id:
				continue
			forwarding_table[0][i] = min(rcv_vec[i]+forwarding_table[0][rcv_id], forwarding_table[0][i])
'''

'''
TODO
[] output message only to target
[] print "forward" transit nodes
[] NU forwarded to all connections
	- except if forwarding table already up-to-date
[] Handle multiple optimal paths
[] "finale" keyword with the last node being informed
[x] forwarding table
[x] routing algorithm -> bellman-fort, distant vector algorithm
[x] Nodes know name of all other nodes
[x] Nodes know only IP of neighbours
[x] Node name given by NTU
[] Nodes open connection only to transmit message, than close.
'''
