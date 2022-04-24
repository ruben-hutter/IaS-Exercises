# terminate all peers by pid
import json

def main():
    with open('sub_procs.json', 'r') as f:
        sub_procs = json.load(f)
    for _, pid in sub_procs.items():
        print(f'kill: {pid}')

# file run
if __name__ == "__main__":
	main()
