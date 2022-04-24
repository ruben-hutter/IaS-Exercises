# terminate all peers by pid
import json

def main():
    with open('sub_procs.json', 'r') as f:
        sub_procs = json.load(f)
    for k, v in sub_procs.items():
        print(f'k: {k} -> {v}')

# file run
if __name__ == "__main__":
	main()
