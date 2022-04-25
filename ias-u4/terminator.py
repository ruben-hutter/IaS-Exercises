# terminate all peers by pid
import subprocess
import json
import os

def main():
    with open('sub_procs.json', 'r') as f:
        sub_procs = json.load(f)
    for pid in sub_procs.values():
        os.kill(int(pid), 9)
        print(f'killed: {pid}')
    
    # ensure to kill processes only once
    subprocess.run(['rm', 'sub_procs.json'])

# file run
if __name__ == "__main__":
	main()
