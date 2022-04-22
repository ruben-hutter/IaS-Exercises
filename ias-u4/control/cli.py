from commands import Commands
from protocol import Protocol
from sender import Sender
from controller import Controller

# cli for user input
class Cli:
	# run the cli
	@staticmethod
	def run():
		while True:
			cmd = input('Enter command: ')
			if cmd.startswith(Commands.MESSAGE):
				tokens = cmd.split(' ')[1:]
				if len(tokens) < 3:
					print(f'> Invalid args! Usage: {Protocol.MESSAGE} <sender:id> <receiver_id> <message>')
					continue
				message = Protocol.MESSAGE + ':'.join(tokens[:2]) + ':' + ' '.join(tokens[2:])
				Sender.send_msg(tokens[0], message)
				continue
			if cmd.startswith(Commands.TOPOLOGY_UPDATE):
				if len(tokens) != 2:
					print(f'> Invalid args! Usage: {Protocol.TOPOLOGY_UPDATE} <config_file>')
					continue
				Controller.topology_update()