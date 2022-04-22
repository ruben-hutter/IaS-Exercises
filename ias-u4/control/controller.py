import parser

# update the networks topology according to the passed config file
def topology_update(config_file):
	# read config and update peers
	parser.parse_file(config_file)