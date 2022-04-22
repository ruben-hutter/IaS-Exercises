# launcher code for automatically launching nodes from a config
import sys
import subprocess

def main(args):
	# launch controller
	if len(args) == 2:
		config = args[1]
		subprocess.run(['python', 'control.py', config])
		return

	# launch peers
	if len(args) == 4:
		# open file
		config = open(args[3])
		# read config and launch peers
		skip = True
		for line in config:
			# line is node declaration
			if line.startswith('addr'):
				# split line
				line = line.split(':')
				# get id
				peer_id = line[0][4:]
				#if peer_id == args[1]:
				#	skip == False
				#if peer_id == args[2]:
				#	skip == True
				#if skip:
				#	continue
				# get addr
				peer_addr = line[1]
				# get port
				peer_port = line[2].rstrip()
				# launch peer
				subprocess.run(['python', 'peer.py', peer_addr, peer_port])
		return
	print('> Invalid args:')
	print('> Usage: python launcher.py <first_node> <last_node> <config_file>')
	print('> or')
	print('> Usage: python launcher.py <config_file>')

# file run
if __name__ == "__main__":
	main(sys.argv)
