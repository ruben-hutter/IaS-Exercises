# peer node code goes here...
import socket

def main(ip_addr, port):
	# init socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip_addr, port))
	sock.listen()
	print(f'> Node online on {ip_addr}:{port}.')

	while True:
		# wait for incoming messages
		connection, addr = sock.accept()
		msg = 

if __name__ == "__main__":
