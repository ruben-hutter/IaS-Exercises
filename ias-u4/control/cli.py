from protocol import Protocol
from commands import Commands
import sender
import control

CONTROLLER_ID = 'controller'

# cli for user input
# run the cli
def run():
	running = True
	while running:
		cmd = input('Enter command: ')
		if cmd.startswith(Commands.MESSAGE):
			tokens = cmd.split(' ')[1:]
			if len(tokens) < 3:
				print(f'> Invalid args! Usage: {Protocol.MESSAGE} <sender:id> <receiver_id> <message>')
				continue
			message = Protocol.MESSAGE + ':' + CONTROLLER_ID + ':' + ':'.join(tokens[1:2]) + ':' + ' '.join(tokens[2:])
			sender.send_msg(tokens[0], message)
			continue
		if cmd.startswith(Commands.TOPOLOGY_UPDATE):
			tokens = cmd.split(' ')[1:]
			if len(tokens) != 1:
				print(f'> Invalid args! Usage: {Protocol.TOPOLOGY_UPDATE} <config_file>')
				continue
			control.topology_update(tokens[0])
			continue
		if cmd.startswith(Commands.END):
			print('> Session terminated...')
			running = False
		print('> Unknown command!')
