# peer node code goes here...
from protocol import Protocol
import routing
import sender
import socket
import sys

# sent nu at least once
sent_once = False

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
			msg = peer_sock.recv(1024)
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
		print('> Received topology update from controller')
		# remove al old NTU states
		global sent_once
		sent_once = False
		routing.routing_table.clear()
		routing.peer_addr.clear()
		# parse new NTU
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
		routing.send_nu()

# run ntu
def parse_ntu(ntu_tokens):
	# process this peer's id
	routing.node_id = ntu_tokens[1]
	# process peer names
	names = ntu_tokens[2].split(' ') # ["name1", ...]
	for name in names:
		# empty string
		if not name.strip():
			continue
		routing.add_route(name.strip())

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
		routing.peer_addr[addr_tokens[0]] = (ip_address, port)

	# set own link
	routing.set_rtt(routing.node_id, 0)
	routing.set_next_hop(routing.node_id, routing.node_id)

	# process peer links
	links = ntu_tokens[4].split(',') # ["name1 ttr1", ...]
	for link in links:
		# empty string
		if not link.strip():
			continue
		link_tokens = link.split(' ')
		dest_id = link_tokens[0]
		rtt = int(link_tokens[1])
		routing.set_rtt(dest_id, rtt)
		routing.set_next_hop(dest_id, dest_id)

# process message
def parse_msg(message_tokens):
	if message_tokens[2] == routing.node_id:
		msg = ' '.join(message_tokens[3:])
		print(f'Message received from node {message_tokens[1]}:')
		print(msg)
		return
	message_tokens[1] = routing.node_id
	receiver_id = message_tokens[2]
	forward_msg(receiver_id, ':'.join(message_tokens))

# forward message to specified receiver
def forward_msg(dest_id, msg):
	receiver_id = routing.get_next_hop(dest_id)
	if receiver_id == routing.NO_HOP:
		print(f'> ERROR: No route to node {dest_id} found!')
		return
	sender.send_msg(receiver_id, msg)
	print(f'> {routing.node_id} forwarded message to {receiver_id}')

# process nu
def parse_nu(nu_tokens):
	# origin of nu
	modified = False
	origin_id = nu_tokens[1]
	links = nu_tokens[2].split(',') # ["name1 rtt1", ...]
	for link in links:
		# empty string
		if not link.strip():
			continue
		link_tokens = link.split(' ')
		dest_id = link_tokens[0]
		rtt = link_tokens[1]
		modified |= routing.bellman_ford(origin_id, dest_id, rtt)
	# only send nu if routing table has changed
	global sent_once
	if modified or not sent_once:
		sent_once = True
		routing.send_nu()

# peer launched
def main(args):
	ip_addr = args[1]
	port = int(args[2])
	launch(ip_addr, port)

# file run
if __name__ == "__main__":
	main(sys.argv)