import socket

# sends messages over tcp
class Sender:
	peer_addresses = {}

	# return a peers address
	@staticmethod
	def get_peer(peer_id):
		return peer_addresses[peer_id]

	# adds a peer to the peer list
	@staticmethod
	def add_peer(peer_id, peer_addr, peer_port):
		peer_addresses[peer_id] = (peer_addr,peer_port)

	# sed message to address
	@staticmethod
	def send_msg(peer_id, msg):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(peer_addresses[peer_id])
			sock.send(msg.encode())
			sock.close()
			print(f'> {peer_id}@{str(peer_addresses[peer_id])}: {msg}')
		except:
			print(f"> ERROR: Couldn't connect to {peer_id}@{str(peer_addresses[peer_id])}!")