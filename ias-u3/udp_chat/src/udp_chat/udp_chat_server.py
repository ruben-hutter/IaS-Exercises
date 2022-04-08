import socket

# constants used for protocol messages
class prot:
	user_handshake = 'hi'
	user_leave = 'by'
	addr_request = 'ar'
	server_handshake = 'hi'

users = {}
rooms = []
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server launched on specified port
def launch(serv_port):
	# create socket
	serv_socket.bind(('0.0.0.0', serv_port))
	print('> Server listening for incoming requests...')
	# receive and parse messages
	while True:
		# receive bytes and address pair
		bytes_and_addr = serv_socket.recvfrom(1024)
		# split into bytes and address
		clnt_msg = bytes_and_addr[0]
		clnt_addr = bytes_and_addr[1]
		parse_msg(clnt_msg, clnt_addr)

# parses received message
def parse_msg(clnt_msg, clnt_addr):
	# split into tokens
	split_msg = clnt_msg.decode().split()
	command = split_msg[0]
	match command:
		case prot.user_handshake:
			# new user registering to server
			if len(split_msg) == 2:
				u_name = split_msg[1]
				negotiate_username(clnt_addr, u_name)
			# ignore if invalid args
		case prot.user_leave:
			# existing user wants to leave server
			send_msg(clnt_addr, prot.user_leave)
			remove_user(clnt_addr)

# send message as text to specified receiver
def send_msg(clnt_addr, serv_msg):
	serv_socket.sendto(serv_msg.encode(), clnt_addr)

# negoatiation of username with new clients
def negotiate_username(clnt_addr, u_name):
	if u_name in users:
		# username already taken -> decline with prot.server_handshake without username
		send_msg(clnt_addr, prot.server_handshake)
		return
	# username free -> ack username with prot.server_handshake + accepted username
	add_user(clnt_addr, u_name)
	send_msg(clnt_addr, prot.server_handshake+' '+u_name)

# add user to users
def add_user(clnt_addr, u_name):
	users[u_name] = clnt_addr
	print('> Add user: '+u_name)

# remove user from users
def remove_user(clnt_addr):
	del_name
	for u_name, u_addr in users.items():
		if u_addr  == clnt_addr:
			del_name = u_name
			break
	del users[del_name]
	print('Removed user: '+u_name)
