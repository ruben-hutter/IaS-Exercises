# peer node code goes here...
import socket
from turtle import forward

from pyparsing import col

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

class DistanceVector:
	forwarding_table = []

	# update of least cost from x to y
	def update_dist(rcv_id, rcv_vec):
		for i in range(1,len(forwarding_table)):
			if i == rcv_id:
				continue
			forwarding_table[0][i] = min(rcv_vec[i]+forwarding_table[0][rcv_id], forwarding_table[0][i])

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
[] Nodes know name of all other nodes
[] Nodes know only IP of neighbours
[] Node name given by NTU
[] Nodes open connection only to transmit message, than close.
'''