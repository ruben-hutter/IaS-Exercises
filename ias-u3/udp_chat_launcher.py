# udp chat driver code goes here
import udp_chat_server
import udp_chat_client
import sys

if __name__ == "__main__":
	# if only prt given -> start as server
	if len(sys.argv) == 2:
		serv_port = int(sys.argv[1])
		udp_chat_server.launch(serv_port)
	# if ip address and port given -> start as client
	if len(sys.argv) == 3:
		serv_ip_addr = sys.argv[1]
		serv_port = int(sys.argv[2])
		udp_chat_client.launch(serv_ip_addr, serv_port)

