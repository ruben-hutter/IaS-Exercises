import protocol
import sender
import commands
import control

# cli for user input
# run the cli
def run():
	while True:
		cmd = input('Enter command: ')
		if cmd.startswith(commands.MESSAGE):
			tokens = cmd.split(' ')[1:]
			if len(tokens) < 3:
				print(f'> Invalid args! Usage: {protocol.MESSAGE} <sender:id> <receiver_id> <message>')
				continue
			message = protocol.MESSAGE + ':'.join(tokens[:2]) + ':' + ' '.join(tokens[2:])
			sender.send_msg(tokens[0], message)
			continue
		if cmd.startswith(commands.TOPOLOGY_UPDATE):
			if len(tokens) != 1:
				print(f'> Invalid args! Usage: {protocol.TOPOLOGY_UPDATE} <config_file>')
				continue
			control.topology_update(tokens[0])
