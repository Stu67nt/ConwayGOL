from colorama import just_fix_windows_console  # Fixes Issue with ANSII codes not working
import numpy as np
import random
import fpstimer
import os
import time
import copy

def generate_initial_cells(x:int=100, y:int=50): # [y,x] coordinate system
    """
    Generates the inital grid for the simulation.
    :param x: length of the grid
    :param y: height of the grid
    :return: 2D list of the filled grid with 1/0. 1 means alive 0 means empty.
    """
    COLOURS = ["\x1b[31m",  # RED
               "\x1b[32m",  # GREEN
               "\x1b[33m", 	# YELLOW
               "\x1b[34m",  # BLUE
               "\x1b[35m",  # MAGENTA
               "\x1b[36m",	# CYAN
               "\x1b[37m",  # WHITE
    ]
    grid = [[None for _ in range(x)] for _ in range(y)]
    x_len = len(grid[0])
    for row_i in range(0, len(grid)):
        grid[row_i] = random.choices([0,1], weights = [90, 10], k=x_len)
        for column_i in range(0, len(grid[row_i])):
            grid[row_i][column_i] = [grid[row_i][column_i],
                                     random.choices((COLOURS), weights = [2, 2, 2, 2, 2, 2, 88], k=1)[0]]
    return grid

def colourmap_grid(grid, colourmap):
    """

    :param grid:
    :param colourmap:
    :return:
    """
    for row_i in range(0, len(grid)):
        for column_i in range(0, len(grid[row_i])):
            if grid[row_i][column_i][0] == 1:
                grid[row_i][column_i][0] = "@"
            else:
                grid[row_i][column_i][0] = " "
    return grid

def draw_grid(grid):
    RESET = "\x1b[0m"

    for row in grid:
        print("".join(f"{char[1]}{char[0]}{RESET}" for char in row))

def check_state(grid, row_i, column_i, state="Normal"):
    cell_char = grid[row_i][column_i][0]
    live_neighbours = 0

    grid_height = len(grid)
    grid_len = len(grid[0])

    # CHANGE PLEASE
    if row_i != 0 and column_i != 0 and grid[row_i - 1][column_i - 1][0] == "@":
        live_neighbours += 1
    if row_i != 0 and grid[row_i - 1][column_i][0] == "@" :
        live_neighbours += 1
    if row_i != 0 and column_i != grid_len-1 and grid[row_i - 1][column_i + 1][0] == "@":
        live_neighbours += 1
    if column_i != 0 and grid[row_i][column_i - 1][0] == "@":
        live_neighbours += 1
    if column_i != grid_len-1 and grid[row_i][column_i + 1][0] == "@":
        live_neighbours += 1
    if row_i != grid_height-1 and column_i != 0 and grid[row_i + 1][column_i - 1][0] == "@":
        live_neighbours += 1
    if row_i != grid_height-1 and grid[row_i + 1][column_i][0] == "@":
        live_neighbours += 1
    if row_i != grid_height-1 and column_i != grid_len-1 and grid[row_i + 1][column_i + 1][0] == "@":
        live_neighbours += 1
    pass

    if state in ["Normal", "Heat"]:
        if live_neighbours > 3:  # Overpopulation
            cell_char = " "
        elif 2 <= live_neighbours <= 3:  # Mantained population
            cell_char = cell_char
        elif live_neighbours < 2:  # Underpopulation
            cell_char = " "

        # Reproduction
        if live_neighbours == 3 and cell_char == " ":
            cell_char = "@"
        elif live_neighbours == 2 and cell_char == " " and state == "Heat":
            cell_char = "@"
        return cell_char

    if state == "Famine":
        if live_neighbours > 2:  # Overpopulation
            cell_char = " "
        elif live_neighbours == 2:  # Mantained population
            cell_char = cell_char
        elif live_neighbours < 2:  # Underpopulation
            cell_char = " "

    return cell_char

def main():
    just_fix_windows_console()  # Needed as otherwise ANSII Escape codes bug out.
    COLOURMAP = [" ", "@"]
    EVENTS, EVENT_WEIGHTS = ["Normal", "Famine", "Heat"], [247, 1, 2]
    gen = 0

    try:
        x, y = os.get_terminal_size()
    except OSError:
        x, y = (20, 20)

    grid = generate_initial_cells(x, y-3)
    grid = colourmap_grid(grid=grid, colourmap= COLOURMAP)

    draw_grid(grid)
    print(f"Generation: {gen}")
    reset = input("Reset Grid? ")

    os.system('cls' if os.name == 'nt' else 'clear')
    if reset == "r":
        return -1

    for gen in range(1,1001):
        current_event = random.choices((EVENTS), weights = EVENT_WEIGHTS, k=1)[0]
        if current_event == "Normal":
            event_text = "Just a Normal Day :D"
        elif current_event == "Famine":
            event_text = "Food Supplies are Dwindling"
        elif current_event == "Heat":
            event_text = "Love is in the air"
        """
        elif current_event == "Thanos Snap":
            event_text = "Thanos Gathered the Infinity Stones"
        elif current_event == "Acid Rain":
            event_text = "This rain is burning"
        """


        if current_event in ["Normal", "Heat", "Famine"]:
            grid_copy = copy.deepcopy(grid)
            for row_i in range(0, len(grid)):
                for column_i in range(0, len(grid[row_i])):
                    grid_copy[row_i][column_i][0] = check_state(grid, row_i, column_i, state = current_event)

        if current_event != "Normal":
            input(event_text)

        grid = copy.deepcopy(grid_copy)
        print("\033[H\033[3J", end="")
        draw_grid(grid)
        print(f"Generation: {gen}     {event_text}")
        """reset = input("")
        if reset == "r":
            break"""

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    x, y = os.get_terminal_size()
    print(x, y)
    is_exit = input("Exit (y/n): ")
    if is_exit == "y":
        break