# peer node code goes here...

# stores the routing table
class Routing:
	routing_table = {}

	# returns the RTT from source to target node
	# -1 is returned if infinite
	def get_rtt(source_id, dest_id):
		if source_id not in routing_table:
			return -1
		if dest_id not in routing_table[source_id]:
			return -1
		return routing_table[source_id][dest_id]

	# sets the specified connections rtt in the routing table
	def set_rtt(source_id, dest_id, rtt):
		routing_table[source_id][dest_id] = rtt
