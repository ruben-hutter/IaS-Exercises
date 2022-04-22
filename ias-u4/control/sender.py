import socket

# sends messages over tcp
peer_addresses = {}

# return a peers address
def get_peer(peer_id):
	return peer_addresses[peer_id]

# adds a peer to the peer list
def add_peer(peer_id, peer_addr, peer_port):
	peer_addresses[peer_id] = (peer_addr, int(peer_port))

# sed message to address
def send_msg(peer_id, msg):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(get_peer(peer_id))
		sock.send(msg.encode())
		sock.close()
		print(f'> {peer_id}@{str(get_peer(peer_id))}: {msg}')
	except:
		print(f"> ERROR: Couldn't connect to {peer_id}@{str(get_peer(peer_id))}!")
