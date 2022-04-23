# control node code goes here
import cli
import parser
import sys

# update the networks topology according to the passed config file
def topology_update(config_file):
	# read config and update peers
	parser.parse_file(config_file)

# peer launched
def main(args):
	config = args[1]
	topology_update(config)
	cli.run()

# file run
if __name__ == "__main__":
        main(sys.argv)
