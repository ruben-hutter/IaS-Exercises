# control node code goes here
import controller
import cli
import sys

# peer launched
def main(args):
	config = args[1]
	controller.topology_update(config)
	cli.run()

# file run
if __name__ == "__main__":
        main(sys.argv)
