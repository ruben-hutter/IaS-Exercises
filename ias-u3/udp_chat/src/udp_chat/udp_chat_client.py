# UDP client implementation goes here
import socket
import sys
import select

# constants for protocol messages
class prot:
	server_handshake = 'hi'
	server_leave = 'by'
	server_addr_request = 'ar'
	client_poke = 'pk'
	server_userlist = 'ul'
	server_roomlist = 'rl'
	server_roomcreate = 'rc'
	server_roomjoin = 'rj'
	server_roomleave = 'rk'
	message = 'msg'

# constants for user commands
class clnt_cmd:
	client_poke = 'poke'
	client_kick = 'kick'
	server_list_rooms = 'roomlist'
	server_list_users = 'userlist'
	server_create_room = 'roomcreate'
	server_join_room = 'roomjoin'
	server_leave_room = 'roomleave'

# socket used for comunication
clnt_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# own username
u_name = ''
# addresses of peers
peers = []
# address of server
serv_addr = ()

# launch udp chat client and connect to server
def launch(serv_ip_addr, serv_port):
	# set server addr
	global serv_addr
	serv_addr = (serv_ip_addr, serv_port)
	# start username negotiation
	negotiate_username(serv_addr)
	# receive and parse messages
	sockets = [sys.stdin, clnt_socket]
	should_run = True
	while should_run:
		# update list of readable sockets
		readables, writables, errors = select.select(sockets, [], [])
		# find and handle client socket
		for socket in readables:
			if socket == clnt_socket:
				# receive data from socket
				bytes_and_addr = socket.recvfrom(1024)
				if not bytes_and_addr:
					print('> Connection closed.')
					should_run = False
					break
				else:
					# parse received message
					msg = bytes_and_addr[0]
					addr = bytes_and_addr[1]
					parse_msg(addr, msg)
			else:
				# read user input from cli
				msg = sys.stdin.readline()
				# parse user input
				if msg[0] == '$':
					# is command
					parse_cmd(msg[1:])
				else:
					# is chat message
					send_chat(msg)
	clnt_socket.close()

# sends the message to the specified adress
def send_msg(addr, clnt_msg):
	clnt_socket.sendto(clnt_msg.encode(), addr)

# send chatmessage to peer(s)
def send_chat(chat_msg):
	msg = prot.message + ' ' + u_name + '> ' + chat_msg
	for addr in peers:
		clnt_socket.sendto(msg.encode(), addr)

# parse incomming messages
def parse_msg(addr, msg):
	# split into tokens
	split_msg = msg.decode().split()
	command = split_msg[0]

	if command == prot.server_addr_request:
		# requested user doesn't exist
		if len(split_msg) ==  1:
			print("> Requested user doesn't exist.")
			return
		# user exists -> establish conection
		add_peer((split_msg[1],int(split_msg[2])))
	elif command == prot.server_userlist:
		# no users online
		if len(split_msg) == 1:
			print('> No users online.')
			return
		# print users to cmd
		if len(split_msg) == 2:
			print('- ' + split_msg[1])
	elif command == prot.server_roomlist:
		# no rooms available
		if len(split_msg) == 1:
			print('> There are no rooms on this server. Create on with $roomcreate <roomname>.')
			return
		# print roomlist to cmd
		if len(split_msg) == 2:
			print('- ' + split_msg[1])
	elif command == prot.server_roomcreate:
		# if invalid request
		if len(split_msg) == 1:
			print('> Room already exists.')
			return
		if len(split_msg) == 2:
			print('> Room created successfully.')
	elif command == prot.server_roomjoin:
		# room doesn't exist
		if len(split_msg) == 1:
			print('No room with this name found.')
			return
		if split_msg[1] == '__clear_peers__':
			peers.clear()
			return
		add_peer((split_msg[1], int(split_msg[2])))
	elif command == prot.message:
		# message to print to cli
		if len(split_msg) == 1:
			# empty message -> ignore
			return
		if not addr in peers and not peers :
			add_peer(addr)
		print(' '.join(split_msg[1:]))

# parse user commands
def parse_cmd(cmd):
	# split  into tokens
	split_cmd = cmd.split()
	command = split_cmd[0]

	if command == clnt_cmd.server_list_rooms:
		# request room list from server
		send_msg(serv_addr, prot.server_roomlist)
	elif command == clnt_cmd.server_list_users:
		# request client list from server
		send_msg(serv_addr, prot.server_userlist)
	elif command == clnt_cmd.client_poke:
		# poke user with certain username
		if len(split_cmd) == 2:
			send_msg(serv_addr, prot.server_addr_request+' '+split_cmd[1])
		else:
			print ('> Invalid args! Usage: $poke <username>')
	elif command == clnt_cmd.client_kick:
		# throw users out of peers list
		peers.clear()
		print('> Removed all peers.')
	elif command == clnt_cmd.server_create_room:
		# request room creation on server
		if len(split_cmd) == 2:
			send_msg(serv_addr, prot.server_roomcreate+' '+split_cmd[1])
		else:
			print('> Invalis args! Usage: $roomcreate <roomname>')
	elif command == clnt_cmd.server_join_room:
		# request joining a room
		if len(split_cmd) == 2:
			send_msg(serv_addr, prot.server_roomjoin+' '+split_cmd[1])
		else:
			print('> Invalid args! Usage: $roomjoin <roomname>')
	elif command == clnt_cmd.server_leave_room:
		# leave room
		send_msg(serv_addr, prot.server_roomleave)
	else:
		# invalid command
		print('> " '+command+' is not a valid command.')

# negotiate a username with the server
def negotiate_username(serv_addr):
	# continue negotiation until aggreable userbame is found
	global u_name
	while u_name == '':
		while True:
			# let user enter username
			username = input('> Enter your username (min length 4 without whitespaces):\n')
			# check if username is valid
			if not (' ' in username) and len(username) > 3:
				# probable username found sent to server
				break
			print ('> Invalid username! Please try again.')
		# try handshake with server under entered username
		msg = prot.server_handshake + ' ' + username
		send_msg(serv_addr, msg)
		# wait for response from server
		while True:
			# receive bytes and address pair
			bytes_and_addr = clnt_socket.recvfrom(1024)
			# split into bytes and address
			s_msg = bytes_and_addr[0]
			s_addr = bytes_and_addr[1]
			# parse response
			# split into tokens
			split_msg = s_msg.decode().split()
			command = split_msg[0]
			# check if message is from server
			if s_addr == serv_addr and command == 'hi':
				# check if server accepted the username
				if len(split_msg) == 1:
					print('> Username ' + username + ' is already taken. Choose another one.')
				else:
					print('> Welcome ' + username + ' to the server.')
					# set username
					u_name = username
				break

# add peer to peers
def add_peer(p_addr):
	peers.append(p_addr)

