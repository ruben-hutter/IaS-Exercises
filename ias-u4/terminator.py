# terminate all peers by pid
import json

def main():
    with open('sub_procs.json', 'r') as f:
        sub_procs = json.load(f)
    for peer, v in sub_procs:
        print(peer, v)

# file run
if __name__ == "__main__":
	main()
