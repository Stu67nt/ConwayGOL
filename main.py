import os
import Evented as e
import Classic as c

def run():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')

		mode = ""
		while mode.lower() not in ["e", "c"]:
			mode = input("Select mode Events/Classic (e/c): ")

		modify_weights = ""
		while modify_weights.lower() not in ["y", "n"]:
			modify_weights = input("Modify Weights (y/n): ")

		values = {}
		if mode.lower() == "e":
			# Used ai for this cause im lazy
			if modify_weights == "y":
				fields = [
					("gens", "Enter num of generations to simulate"),
					("dead", "Dead Cell Weight"),
					("alive", "Alive Cell Weight"),
					("bomb", "Bomb Cell Weight"),
					("normal", "Normal Gen Weight"),
					("famine", "Famine Gen Weight"),
					("love", "Love Gen Weight"),
				]

				for key, prompt in fields:
					while True:
						val = input(f"{prompt}: ")
						if val.isdigit():
							values[key] = int(val)
							break
						print("Please enter a valid integer.")

				e.main(
					total_gens=values["gens"],
					event_weights=[
						values["normal"],
						values["famine"],
						values["love"],
					],
					cell_weights=[
						values["dead"],
						values["alive"],
						values["bomb"],
					]
				)
			else:
				e.main()

		elif mode.lower() == "c":
			if modify_weights == "y":
				fields = [
					("gens", "Enter num of generations to simulate"),
					("dead", "Dead Cell Weight"),
					("alive", "Alive Cell Weight")
				]

				for key, prompt in fields:
					while True:
						val = input(f"{prompt}: ")
						if val.isdigit():
							values[key] = int(val)
							break
						print("Please enter a valid number.")
				c.main(total_gens=values["gens"],
					   cell_weights=[values["dead"], values["alive"]])
			else:
				c.main()

		is_exit = input("Exit (y/n): ")
		if is_exit == "y":
			break

if __name__ == "__main__":
	run()