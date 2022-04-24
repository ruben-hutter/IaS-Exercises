# terminate all peers by pid
import json
import os

def main():
    with open('sub_procs.json', 'r') as f:
        sub_procs = json.load(f)
    for _, pid in sub_procs.items():
        os.kill(int(pid), 9)
        print(f'killed: {pid}')

# file run
if __name__ == "__main__":
	main()
