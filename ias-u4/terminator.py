# terminate all peers by pid
import json

def main():
    with open('sub_procs.json', 'r') as f:
        sub_procs = json.load(f)
    print(sub_procs, type(sub_procs))

# file run
if __name__ == "__main__":
	main()
