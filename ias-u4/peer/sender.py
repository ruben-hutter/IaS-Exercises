import socket
import routing

# send message to receiver with specified id
def send_msg(dest_id, msg):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect(routing.peer_addr[dest_id])
		sock.send(msg.encode())
		sock.close()
	except:
		print(f"> ERROR: Couldn't connect to {dest_id}@{str(routing.peer_addr[dest_id])}!")

# broadcast message to all neighbours
def broadcast_msg(msg):
	for dest_id in routing.peer_addr:
		send_msg(dest_id, msg)
