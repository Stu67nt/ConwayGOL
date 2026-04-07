"""
Look at evented.py for funtion explanations.
"""

from colorama import just_fix_windows_console  # Fixes Issue with ANSII codes not working
import random
import os
import time

def generate_initial_cells(x:int=100, y:int=50, cell_weights = [92, 8]): # [y,x] coordinate system
    grid = [[None for _ in range(x)] for _ in range(y)]
    x_len = len(grid[0])
    for row_i in range(0, len(grid)):
        grid[row_i] = random.choices([0,1], weights = cell_weights, k=x_len)
    return grid

def colourmap_grid(grid):
    for row_i in range(0, len(grid)):
        for column_i in range(0, len(grid[row_i])):
            if grid[row_i][column_i] == 1:
                grid[row_i][column_i] = "@"
            else:
                grid[row_i][column_i] = " "
    return grid

def draw_grid(grid):
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

def main(total_gens = 1000, cell_weights = [92, 8]):
    just_fix_windows_console()  # Needed as otherwise ANSII Escape codes bug out.
    gen = 0
    reset = "r"
    while reset == "r":
        try:
            x, y = os.get_terminal_size()
        except OSError:
            x, y = (20, 20)

        grid = generate_initial_cells(x, y-3, cell_weights = cell_weights)
        grid = colourmap_grid(grid=grid)

        draw_grid(grid)
        print(f"Generation: {gen}")
        reset = input("Reset Grid (r)? ")

        os.system('cls' if os.name == 'nt' else 'clear')

    for gen in range(1,total_gens+1):
        grid_copy = [row[:] for row in grid]
        for row_i in range(0, len(grid)):
            for column_i in range(0, len(grid[row_i])):
                grid_copy[row_i][column_i] = check_state(grid, row_i, column_i)
        grid = [row[:] for row in grid_copy]
        print("\033[H\033[3J", end="")
        draw_grid(grid)
        print(f"Generation: {gen}")
    input("Press enter to proceed")

if __name__ == "__main__":
    main()