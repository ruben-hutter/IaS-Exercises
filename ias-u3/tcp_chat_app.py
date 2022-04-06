# chat application using tcp
import sys
import tcp_chat

def main(ip_addr, port):
	client = Client(ip_addr, port)
	client.listen()
	client.write()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ('Invalid arguments! \n Usage: ./tcp_chat_app.py <ip_address> <port>')
		exit()
	ip_addr = sys.argv[1]
	port = sys.argv[2]
	main(ip_addr, port)

