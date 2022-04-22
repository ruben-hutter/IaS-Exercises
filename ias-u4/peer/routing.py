# stores the routing table
class Routing:

	INFINITE = -1
	NO_HOP = ''

	node_id = '' # id of this node
	peer_addr = {} # {dest_id:(ip,port), ...}
	routing_table = {} # {dest_id:[rtt, next_hop], ...}

	# add entry to routing table
	@staticmethod
	def add_route(dest_id):
		routing_table[dest_id] = [INFINITE, NO_HOP]

	# returns the RTT to destination, or Routing.INFINITE
	@staticmethod
	def get_rtt(dest_id):
		return routing_table[dest_id][0]

	# set rtt to destination
	@staticmethod
	def set_rtt(dest_id, rtt):
		routing_table[dest_id][0] = int(rtt)

	# return next hop to destination, or ROUTING.NO_HOP
	@staticmethod
	def get_next_hop(dest_id):
		return routing_table[dest_id][1]

	# set next hop to destination
	@staticmethod
	def set_next_hop(dest_id, next_hop_id):
		routing_table[dest_id][1] = next_hop_id

	# send nu to peers
	def send_nu():
		return