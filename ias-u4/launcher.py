# launcher code for automatically launching nodes from a config
import json
import sys
import subprocess

def main(args):
	if len(args) != 3:
		print('> Invalid args! Usage: python launcher.py <controller/peers> <config>')
		return

	modus = args[1]
	config = args[2]

	# launch controller: "python launcher.py controller config"
	if modus == "controller":
		subprocess.run([sys.executable, 'control/control.py', config])
	
	# launch peers: "python launcher.py peers config"
	elif modus == "peers":
		# open config file
		config = open(config)
		# save subprocesses
		sub_procs = {}
		# read config and launch peers
		for line in config:
			# line is node declaration
			if line.startswith('addr'):
				# split line
				line = line.split(':') # ["addr", "ip_addr", "port"]
				peer_id = line[0][4:]
				peer_addr = line[1]
				peer_port = line[2]
				# launch peer
				p = subprocess.Popen([sys.executable, 'peer/peer.py', peer_addr, peer_port])
				sub_procs[peer_id] = p.pid
		# save subprocesses to a file
		with open('sub_procs.json', 'w') as fp:
			json.dump(sub_procs, fp,  indent=4)

# file run
if __name__ == "__main__":
	main(sys.argv)
