# UDP client implementation goes here
import socket

# constants for server protocol messages
SERVER_HANDSHAKE = 'hi'
SERVER_LEAVE = 'by'
SERVER_ADDRESS_REQUEST = 'ar'

clnt_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
u_name = ''

# launch udp chat client and connect to server
def launch(serv_ip_addr, serv_port):
	# start username negotiation
	negotiate_username(serv_ip_addr, serv_port)
	# receive and parse messages
	while True:
		# receive bytes and address pair
		bytes_and_addr = clnt_socket.recvfrom(1024)
		# split into bytes and address
		msg = bytes_and_addr[0]
		addr = bytes_and_addr[1]
		parse_msg(addr, msg)

# sends the message to the specified adress
def send_msg(addr, clnt_msg):
	clnt_socket.sendto(clnt_msg.encode(), addr)

# parse incomming messages
def parse_msg(addr, msg):
	# split into tokens
        split_msg = clnt_msg.encode().split()
        command = split_msg[0]

# negotiate a username with the server
def negotiate_username(serv_ip_addr, serv_port):
	# continue negotiation until aggreable userbame is found
	global u_name
	while u_name == '':
		while True:
			# let user enter username
			username = input('Enter your username (min length 4 without whitespaces):\n')
			# check if username is valid
			if username != ' ' and len(username) > 3:
				# probable username found sent to server
				break
			print ('> Invalid username! Please try again.')
		# try handshake with server under entered username
		msg = SERVER_HANDSHAKE + ' ' + username
		send_msg((serv_ip_addr, serv_port), msg)
		# wait for response from server
		while True:
			# receive bytes and address pair
			bytes_and_addr = clnt_socket.recvfrom(1024)
			# split into bytes and address
			serv_msg = bytes_and_addr[0]
			serv_addr = bytes_and_addr[1]
			# parse response
			# split into tokens
			split_msg = serv_msg.decode().split()
			command = split_msg[0]
			# check if message is from server
			if serv_addr == (serv_ip_addr,serv_port) and command == 'hi':
				# check if server accepted the username
				if len(split_msg) == 1:
					print('> Username ' + username + ' is already taken. Choose another one.')
				else:
					print('> Welcome ' + username + ' to the server.')
					# set username
					u_name = username
				break
