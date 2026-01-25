from colorama import just_fix_windows_console  # Fixes Issue with ANSII codes not working
import numpy as np
import random
import fpstimer
import os

def generate_initial_cells(x:int=100, y:int=50): # [y,x] coordinate system
    grid = [[None for _ in range(x)] for _ in range(y)]
    x_len = len(grid[0])
    for row_i in range(0, len(grid)):
        grid[row_i] = random.choices([0,1], weights = [90, 10], k=x_len)
    return grid

def colourmap_grid(grid, colourmap):
    for row_i in range(0, len(grid)):
        for column_i in range(0, len(grid[row_i])):
            if grid[row_i][column_i] == 1:
                grid[row_i][column_i] = "@"
            else:
                grid[row_i][column_i] = " "
    return grid

def draw_grid(grid):
    # print("\033[H\033[3J", end="")
    for row in grid:
        print("".join(char for char in row))


def check_state(grid, row_i, column_i):
    cell_char = grid[row_i][column_i]
    live_neighbours = 0

    grid_height = len(grid)
    grid_len = len(grid[0])

    # CHANGE PLEASE
    if row_i != 0 and column_i != 0 and grid[row_i - 1][column_i - 1] == "@":
        live_neighbours += 1
    if row_i != 0 and grid[row_i - 1][column_i] == "@" :
        live_neighbours += 1
    if row_i != 0 and column_i != grid_len-1 and grid[row_i - 1][column_i + 1] == "@":
        live_neighbours += 1
    if column_i != 0 and grid[row_i][column_i - 1] == "@":
        live_neighbours += 1
    if column_i != grid_len-1 and grid[row_i][column_i + 1] == "@":
        live_neighbours += 1
    if row_i != grid_height-1 and column_i != 0 and grid[row_i + 1][column_i - 1] == "@":
        live_neighbours += 1
    if row_i != grid_height-1 and grid[row_i + 1][column_i] == "@":
        live_neighbours += 1
    if row_i != grid_height-1 and column_i != grid_len-1 and grid[row_i + 1][column_i + 1] == "@":
        live_neighbours += 1

    if live_neighbours > 3:  # Overpopulation
        cell_char = " "
    elif 2 <= live_neighbours <= 3:  # Mantained population
        cell_char = cell_char
    elif live_neighbours < 2:  # Underpopulation
        cell_char = " "

    # Reproduction
    if live_neighbours == 3 and cell_char == " ":
        cell_char = "@"

    return cell_char

def main():
    just_fix_windows_console()  # Needed as otherwise ANSII Escape codes bug out.
    COLOURMAP = [" ", "@"]
    timer = fpstimer.FPSTimer(10)
    x, y = os.get_terminal_size()
    gen = 0

    grid = generate_initial_cells(x, y-3)
    grid = colourmap_grid(grid = grid, colourmap= COLOURMAP)

    draw_grid(grid)
    print(f"Generation: {gen}")
    reset = input()
    if reset == "r":
        # ANSII escape character. Moves cursor to the top of the terminal and clears everything below cursor.
        print("\033[H\033[3J", end="")
        return -1

    for gen in range(1,1001):
        grid_copy = [row[:] for row in grid]
        for row_i in range(0, len(grid)):
            for column_i in range(0, len(grid[row_i])):
                grid_copy[row_i][column_i] = check_state(grid, row_i, column_i)
        print("\033[H\033[3J", end="")
        draw_grid(grid)
        print(f"Generation: {gen}")

        grid = [row[:] for row in grid_copy]
        timer.sleep()


while True:
    main()