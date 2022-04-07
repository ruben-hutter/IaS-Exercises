# UDP server implementation goes here
import socket

# dict containing all online users
users = []
serv_sock

# server launched on specified port
def launch(serv_port):
	# create socket
	serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	serv_socket.bind('0.0.0.0', serv_port)
	print('> Server listening for incoming requests...')
	# receive and parse messages
	while True:
		# receive bytes and address pair
		bytes_and_addr = serv_socket.recvfrom(1024)
		# split into bytes and address
		clnt_msg = bytes_and_addr[0]
		clnt_addr = bytes_and_addr[1]

# parses received message
def parse_msg(clnt_msg, clnt_addr ):
	# split into tokens
	split_msg = clnt_msg.encode().split()
	command = split_msg[0]
	match command:
		case 'hi':
			# new user registering to server
			if len(split_msg) = 2:
				u_name = 

		case 'by':
			# exiting user user leaving server

		case 'in'
			# existing user wants addr to  other user

# send message as text to specified receiver
def send_msg(clnt_addr, serv_msg):
	serv_sock.sendto(serv_msg.encode(), clnt_addr)
