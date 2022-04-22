import sender

INFINITE = -1
NO_HOP = ''

node_id = '' # id of this node
peer_addr = {} # {dest_id:(ip,port), ...}
routing_table = {} # {dest_id:[rtt, next_hop], ...}

# add entry to routing table
def add_route(dest_id):
	routing_table[dest_id] = [INFINITE, NO_HOP]

# returns the RTT to destination, or Routing.INFINITE
def get_rtt(dest_id):
	return routing_table[dest_id][0]

# set rtt to destination
def set_rtt(dest_id, rtt):
	routing_table[dest_id][0] = int(rtt)

# return next hop to destination, or ROUTING.NO_HOP
def get_next_hop(dest_id):
	return routing_table[dest_id][1]

# set next hop to destination
def set_next_hop(dest_id, next_hop_id):
	routing_table[dest_id][1] = next_hop_id

# send nu to peers
def send_nu(): # NU:origin_id:name1 rtt, ...
	nu_msg = "NU:" + node_id + ':'
	for dest_id, link_info in routing_table.items():
		# skip unreachable
		if link_info[1] == NO_HOP:
			continue
		nu_msg += dest_id + ' ' + link_info[0] + ','
	sender.broadcast_msg(nu_msg)
