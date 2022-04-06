# chat application using tcp
import sys
import tcp_chat.src.tcp_chat as tcp_chat # import tcp_chat

def main(ip_addr, r_port, listen_port):
	client = tcp_chat.client.Client(ip_addr, r_port, listen_port)
	client.connect()
	client.start_sender()

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print ('Invalid arguments! \n Usage: ./tcp_chat_app.py <receiver_address> <receiver_port> <listening_port>')
		exit()
	ip_addr = sys.argv[1]
	r_port = sys.argv[2]
	listen_port = sys.argv[3]
	main(ip_addr, r_port, listen_port)
