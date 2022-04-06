# code for receiver goes here
class Receiver:

	def listen_for_clients(self, port):
		# create new socket
		self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# bind socket to host and known port
		self.s_socket.bind((socket.gethostname(), port))
		# makes socket to server socket
		self.s_socket.listen(5)
		while True:
			# accept connections
			(r_socket, ip_addr) = s_socket.accept()
			#start printing of messages
			r_thread = Thread(target=receive_messages, args=(r_socket))
			r_thread.deamon = True
			r_thread.start()

	def receive_messages(self, r_socket):
		while True:
			msg = r_socket.recv(1024).decode()
			print('msg\n')
