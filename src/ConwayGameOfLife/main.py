import os
from . import evented as e
from . import classic as c

def run():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')

		mode = ""
		while mode.lower() not in ["e", "c"]:
			mode = input("Select mode Events/Classic (e/c): ")

		modify_weights = ""
		while modify_weights.lower() not in ["y", "n"]:
			modify_weights = input("Modify Weights (y/n): ")

		gens = "None"
		while not gens.isdigit():
			gens = input("Enter number of generations to simulate: ")
		gens = int(gens)

		values = {}
		if mode.lower() == "e":
			if modify_weights == "y":
				fields = [
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
					total_gens=gens,
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
				e.main(total_gens=gens)

		elif mode.lower() == "c":
			if modify_weights == "y":
				fields = [
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
				c.main(total_gens=gens,
					   cell_weights=[values["dead"], values["alive"]])
			else:
				c.main(total_gens=gens)

		is_exit = input("Exit (y/n): ")
		if is_exit == "y":
			break

if __name__ == "__main__":
	run()