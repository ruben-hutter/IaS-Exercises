# launch code for network goes here
import sys
import control_node as cn

def main(args):
	config_file = args[1]
	# only run node range
	if len(args) == 3:
		start_node = args[2]
		end_node = args[3]
	cn.build_network(config_file, start_node, end_node)

# script run as main
if __name__ == '__main__':
	main(sys.argv[1:])
