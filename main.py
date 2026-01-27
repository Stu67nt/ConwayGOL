import os
import Evented as e
import Classic as c

def run():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		choice = ""
		while choice.lower() not in ["e", "c"]:
			choice = input("Select mode Events/Classic (e/c): ")
		if choice.lower() == "e":
			e.main()
		elif choice.lower() == "c":
			c.main()

		is_exit = input("Exit (y/n): ")
		if is_exit == "y":
			break

if __name__ == "__main__":
	run()