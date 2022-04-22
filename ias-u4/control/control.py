# control node code goes here
from cli import Cli
import sys

# update the networks topology according to the passed config file
@staticmethod
def topology_update(config_file):
	# read config and update peers
	Parser.parse_file(config_file)


# peer launched
def main(args):
	config = args[1]
	topology_update(config)
	Cli.run()

# file run
if __name__ == "__main__":
        main(sys.argv)
