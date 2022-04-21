# peer node code goes here...
import socket

# stores the routing table
class Routing:

	INFINITE = -1
	NO_HOP = ''

	node_id = ''
	peer_addr = {}
	routing_table = {}

	# add entry to routing table
	def add_route(dest_id):
		routing_table[dest_id] = [INFINITE, NO_HOP]

	# returns the RTT to destination
	# returns Routing.INFINITE  if no route found
	def get_rtt(dest_id):
		return routing_table[dest_id][0]

	# set rtt to destination
	def set_rtt(dest_id, rtt):
		routing_table[dest_id][0] = rtt

	# return next hop to destination
	# return ROUTING.NO_HOP  if no route found
	def get_next_hop(dest_id):
		return routing_table[dest_id][1]

	# set next hop to destination
	def set_next_hop(dest_id, next_hop_id):
		routing_table[dest_id][1] = next_hop_id

''' 	# update of least cost from x to y
	def update_dist(rcv_id, rcv_vec):
		for i in range(1,len(forwarding_table)):
			if i == rcv_id:
				continue
			forwarding_table[0][i] = min(rcv_vec[i]+forwarding_table[0][rcv_id], forwarding_table[0][i])
'''

'''
TODO
[] output message only to target
[] print "forward" transit nodes
[] NU forwarded to all connections
	- except if forwarding table already up-to-date
[] Handle multiple optimal paths
[] "finale" keyword with the last node being informed
[x] forwarding table
[x] routing algorithm -> bellman-fort, distant vector algorithm
[x] Nodes know name of all other nodes
[x] Nodes know only IP of neighbours
[x] Node name given by NTU
[] Nodes open connection only to transmit message, than close.
'''
