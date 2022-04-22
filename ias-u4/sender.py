class Sender:
	# send message to receiver with specified id
	def send_msg(receiver_id, msg):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(Routing.peer_addr[receiver_id])
		sock.send(msg.encode())
		sock.close()