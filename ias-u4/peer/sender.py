import socket
import routing

# send message to receiver with specified id
def send_msg(dest_id, msg):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(routing.peer_addr[dest_id])
	sock.send(msg.encode())
	sock.close()