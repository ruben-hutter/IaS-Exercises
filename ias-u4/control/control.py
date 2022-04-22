# control node code goes here
from controller import Controller
from cli import Cli
import sys

# peer launched
def main(args):
	config = args[1]
	Controller.topology_update(config)
	Cli.run()

# file run
if __name__ == "__main__":
        main(sys.argv)
