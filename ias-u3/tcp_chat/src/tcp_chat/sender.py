# code for sender goes here
class Sender:
	def __init__():
		self.s_socket = None
	def connect(ip_addr, port):
		# create socket
		s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# connect to other client
		s_socket.connect(ip_addr, port)

	def start_sender():
		while True:
			msh = input()
			if msg == ':q':
				break
			self.s_socket.send(msg.encode())
