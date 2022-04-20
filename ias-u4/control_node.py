# control node code goes here...
import socket

topology = []

# init network to with specified config
def init(config):
	# parse config
	parse_config(config)
	# update nodes
	send_ntu()
	# await user input
	run_cli()

# reads the config an inits the topology accordingly
def parse_config(config):
	# empty topology
	topology.clear()
	# open file
	cfg = open(config)
	for line in cfg.readlines():
		# skip if comment
		if line.startswith('#'):
			continue
		split_line = line.split(':')
		topology.append(Node(split_line[1], split_line[2], get_peers(split_line[3])))

# return list of tuples from config section
def get_peers(part):
	peers = []
	for p in part.split(','):
		peers.append(get_tuple_from_split_part(p))
	return peers

# returns a tuple form config connection
def get_tuple_from_split_part(part):
	split = part.split()
	return (split[0],split()[1])

# send topology update to nodes
def send_ntu()
	for node in topology:
		msg = []
		msg.append('NTU')
		for peer in node.get_peers():
			msg.append(peer[0])
			mas.append(peer[1])
		send_msg(node.get_addr(), ' '.join(msg))

# opens a socket to the specified addres and sends the specified message
def send_msg(addr,msg):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(addr)
	sock.send(msg)
	sock.close()

# run the cli to allow the user to send messages and to reload configs
def run_cli():
	while True:
		split = inpt('Enter command: ').split()
		# user sends message
		if (split[0] == 'MSG'):
			msg = []
			msg.append('MSG')
			# add receiver address: msg.append(...)
			addr = topology[int(split[1])-1].get_addr()
			send_msg(addr, ' '.join(msg))
			continue
		# user calls NTU
		if (split[0] == 'NTU'):
			init(' '.join(split[2:])
			return

# object to store node
class Node:
	addr
	peers = []
	def __init__(self, ip_addr, port, peers):
		self.addr = (ip_addr, port)
		self.peers = peers

	def get_adr():
		return self.addr

	def get_peers():
		return peers
