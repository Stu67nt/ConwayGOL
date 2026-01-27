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
        grid[row_i] = random.choices([0, 1, 2], weights = [899, 100, 1], k=x_len)
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
            elif grid[row_i][column_i][0] == 2:
                grid[row_i][column_i][0] = "X"
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
    explosion_flag = False
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

    if state in ["Normal", "Love"] and cell_char != "X":
        if live_neighbours > 3:  # Overpopulation
            cell_char = " "
        elif 2 <= live_neighbours <= 3:  # Mantained population
            cell_char = cell_char
        elif live_neighbours < 2:  # Underpopulation
            cell_char = " "

    # Reproduction
    if live_neighbours == 3:
        if cell_char != "X":
            cell_char = "@"
        else:
            cell_char = " "
            explosion_flag = True
    elif live_neighbours == 2 and state == "Love":
        if cell_char != "X":
            cell_char = "@"
        else:
            cell_char = " "
            explosion_flag = True


    if state == "Famine" and cell_char != "X":
        if live_neighbours > 2:  # Overpopulation
            cell_char = " "
        elif live_neighbours == 2:  # Mantained population
            cell_char = cell_char
        elif live_neighbours < 2:  # Underpopulation
            cell_char = " "

        # Reproduction
        if live_neighbours == 4:
            if cell_char != "X":
                cell_char = "@"
            else:
                cell_char = " "
                explosion_flag = True

    return cell_char, explosion_flag

def explode_bomb(grid, row_i, column_i):
    grid_height = len(grid)
    grid_len = len(grid[0])

    if row_i != 0 and column_i != 0:
        grid[row_i - 1][column_i - 1][0] == " "
    if row_i != 0:
        grid[row_i - 1][column_i][0] == " "
    if row_i != 0 and column_i != grid_len-1:
        grid[row_i - 1][column_i + 1][0] == " "
    if column_i != 0:
        grid[row_i][column_i - 1][0] == " "
    if column_i != grid_len-1:
        grid[row_i][column_i + 1][0] == " "
    if row_i != grid_height-1 and column_i != 0:
        grid[row_i + 1][column_i - 1][0] == " "
    if row_i != grid_height-1:
        grid[row_i + 1][column_i][0] == " "
    if row_i != grid_height-1 and column_i != grid_len-1:
        grid[row_i + 1][column_i + 1][0] == " "

    return grid

def main():
    just_fix_windows_console()  # Needed as otherwise ANSII Escape codes bug out.
    COLOURMAP = [" ", "@", "X"]
    EVENTS, EVENT_WEIGHTS = ["Normal", "Famine", "Love"], [297, 1, 2]
    gen = 0
    event_start = 1
    reset = "r"

    while reset == "r":
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

    for gen in range(1,1001):
        if event_start not in range(gen-1, random.randint(gen-6, gen-2), -1):
            current_event = random.choices((EVENTS), weights = EVENT_WEIGHTS, k=1)[0]
            if current_event == "Normal":
                event_text = "Just a normal day!"
                event_start = gen
            elif current_event == "Famine":
                event_text = "The hunger grows  "
                event_start = gen
            elif current_event == "Love":
                event_text = "Love is in the air"
                event_start = gen
        else:
            pass


        if current_event in ["Normal", "Love", "Famine"]:
            grid_copy = copy.deepcopy(grid)
            bomb_count = 0
            for row_i in range(0, len(grid)):
                for column_i in range(0, len(grid[row_i])):
                    grid_copy[row_i][column_i][0], explosion_flag = check_state(grid, row_i, column_i, state = current_event)
                    if explosion_flag == True:
                        grid_copy = explode_bomb(grid_copy, row_i, column_i)
                    if grid_copy[row_i][column_i][0] == "X":
                        bomb_count += 1

        grid = copy.deepcopy(grid_copy)
        print("\033[H\033[3J", end="")
        draw_grid(grid)
        print(f"Generation: {gen}  Bombs Remianing: {bomb_count}")
        print(event_text)
        """
        reset = input("")
        if reset == "r":
            break
        """


