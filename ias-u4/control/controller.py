from parser import Parser

class Controller:
	# update the networks topology according to the passed config file
	@staticmethod
	def topology_update(config_file):
		# read config and update peers
		Parser.parse_file(config_file)