# tcp chat driver code goes here
import tcp_chat
import sys

if __name__ == "__main__":
	# if only prt given -> start as server
	if len(sys.argv) == 2:
		serv_port = int(sys.argv[1])
		tcp_chat.launch_server(serv_port)
	# if ip address and port given -> start as client
	if len(sys.argv) == 3:
		serv_ip_addr = sys.argv[1]
		serv_port = int(sys.argv[2])
		tcp_chat.launch_client(serv_ip_addr, serv_port)

