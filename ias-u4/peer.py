# peer node code goes here...
from ipaddress import ip_address
import socket
from this import d

# protocol message prefixes
class Protocol:
	MESSAGE = 'MSG'
	TOPOLOGY_UPDATE = 'NTU'
	FINALE = 'FIN'
	NETWORK_UPDATE = 'NU'

# stores the routing table
class Routing:

	INFINITE = -1
	NO_HOP = ''

	node_id = '' # id of this node
	peer_addr = {} # {dest_id:(ip,port), ...}
	routing_table = {} # {dest_id:[rtt, next_hop], ...}

	# add entry to routing table
	@staticmethod
	def add_route(dest_id):
		routing_table[dest_id] = [INFINITE, NO_HOP]

	# returns the RTT to destination, or Routing.INFINITE
	@staticmethod
	def get_rtt(dest_id):
		return routing_table[dest_id][0]

	# set rtt to destination
	@staticmethod
	def set_rtt(dest_id, rtt):
		routing_table[dest_id][0] = int(rtt)

	# return next hop to destination, or ROUTING.NO_HOP
	@staticmethod
	def get_next_hop(dest_id):
		return routing_table[dest_id][1]

	# set next hop to destination
	@staticmethod
	def set_next_hop(dest_id, next_hop_id):
		routing_table[dest_id][1] = next_hop_id

	# send nu to peers
	def send_nu():
		#TODO implementation

class Sender:
	# send message to receiver with specified id
	def send_msg(receiver_id, msg):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(Routing.peer_addr[receiver_id])
		sock.send(msg.encode())
		sock.close()

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
	# received topology update
	if message.startswith(Protocol.TOPOLOGY_UPDATE):
		parse_ntu(message.split(':'))
		return
	# received normal message to either print or forward
	if message.startswith(Protocol.MESSAGE):
		parse_msg(message.split(':'))
		return
	# received network update from peer
	if message.startswith(Protocol.NETWORK_UPDATE):
		parse_nu(message.split(':'))
		return
	# received finale command from controller
	if message.startswith(Protocol.FINALE):
		Routing.send_nu()

# run ntu
def parse_ntu(ntu_tokens):
	# clear old routing table
	Routing.routing_table.clear()
	# process this peer's id
	Routing.node_id = ntu_tokens[1]
	# process peer names
	names = ntu_tokens[2].split(' ') # ["name1", ...]
	for name in names:
		# empty string
		if not name.strip():
			continue
		Routing.add_route(name.strip())

	# process peer addresses
	addrs = ntu_tokens[3].split(' ') # ["id1_ip1_port1", ...]
	for addr in addrs:
		# empty string
		if not addr.strip():
			continue
		addr_tokens = addr.split('_') # ["id", "ip", "port"]
		# add peer addr to peer addresses
		ip_address = addr_tokens[1]
		port = int(addr_tokens[2])
		Routing.peer_addr[addr_tokens[0]] = (ip_address, port)

	# process peer links
	links = ntu_tokens[4].split(',') # ["name1 ttr1", ...]
	for link in links:
		# empty string
		if not link.strip():
			continue
		link_tokens = link.split(' ')
		dest_id = link_tokens[0]
		rtt = int(link_tokens[1])
		Routing.set_rtt(dest_id, rtt)

# process message
def parse_msg(message_tokens):
	if message_tokens[2] == Routing.node_id:
		msg = ' '.join(message_tokens[3:])
		print(f'Message received from node {message_tokens[1]}:')
		print(msg)
		return
	message_tokens[1] = Routing.node_id
	dest_id = message_tokens[2]
	forward_msg(':'.join(message_tokens), receiver_id)

# forward message to specified receiver
def forward_msg(dest_id, msg):
	receiver_id = Routing.get_next_hop(dest_id)
	Sender.send_msg(receiver_id, msg)
	print(f'> forwarded message to {receiver_id}')

# process nu
def parse_nu(nu_tokens):
	# origin of nu
	origin_id = nu_tokens[1]
	links = nu_tokens[2].split(',') # ["name1 rtt1", ...]
	for link in links:
		link_tokens = link.split(' ')
		dest_id = link_tokens[0]
		rtt = int(link_tokens[1])
		bellman_ford(origin_id, dest_id, rtt)

# Bellman–Ford algorithm
def bellman_ford(origin_id, dest_id, rtt):
	actual_rtt = Routing.routing_table[dest_id][0]
	min_rtt = min(actual_rtt, Routing.routing_table[origin_id] + int(rtt))
	if min_rtt < actual_rtt:
		Routing.routing_table[dest_id][0] = min_rtt
		Routing.routing_table[dest_id][1] = origin_id

'''
TODO
[x] output message only to target
[x] print "forward" transit nodes
[] NU forwarded to all connections
	- except if forwarding table already up-to-date
[] Handle multiple optimal paths
[] "finale" keyword with the last node being informed
[x] forwarding table
[x] routing algorithm -> bellman-fort, distant vector algorithm
[x] Nodes know name of all other nodes
[x] Nodes know only IP of neighbours
[x] Node name given by NTU
[x] Nodes open connection only to transmit message, than close.
'''
