# peer node code goes here...
import socket

# protocol message prefixes
class Protocol:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'
	NETWORK_UPDATE = 'NU'

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
		peer_sock, _ = sock.accept()
		try:
			# receive message from other peer
			msg = peer_sock.recv()
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
		parse_msg(message.split(':'))
		return
	if message.startswith(Protocol.NETWORK_UPDATE):
		parse_nu(message.split(':'))

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
		Routing.peer_addr[addr_tokens[0]] = (addr_tokens[1],int(addr_tokens[2]))
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
	if message_tokens[2] == Routing.node_id:
		msg = ' '.join(message_tokens[3:])
		print(f'Message received from node {message_tokens[1]}:')
		print(msg)
		return
	message_tokens[1] = Routing.node_id
	#forward_msg(':'.join(message_tokens))

# process nu
def parse_nu(nu_tokens):
	return

# stores the routing table
class Routing:

	INFINITE = -1
	NO_HOP = ''

	node_id = ''
	peer_addr = {}
	routing_table = {}

	# add entry to routing table
	@staticmethod
	def add_route(dest_id):
		routing_table[dest_id] = [INFINITE, NO_HOP]

	# returns the RTT to destination
	# returns Routing.INFINITE if no route found
	@staticmethod
	def get_rtt(dest_id):
		return routing_table[dest_id][0]

	# set rtt to destination
	@staticmethod
	def set_rtt(dest_id, rtt):
		routing_table[dest_id][0] = rtt

	# return next hop to destination
	# return ROUTING.NO_HOP if no route found
	@staticmethod
	def get_next_hop(dest_id):
		return routing_table[dest_id][1]

	# set next hop to destination
	@staticmethod
	def set_next_hop(dest_id, next_hop_id):
		routing_table[dest_id][1] = next_hop_id


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
