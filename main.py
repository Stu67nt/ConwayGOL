from colorama import just_fix_windows_console  # Fixes Issue with ANSII codes not working
import numpy as np
import random

def generate_initial_cells(): # [y,x] coordinate system
    grid = np.zeros(shape = (50, 100))
    x_len = len(grid[0])
    for row_i in range(0, len(grid)):
        grid[row_i] = random.choices([0,1], weights = [95, 5], k=x_len)
    return grid.astype("uint8")

def colourmap_grid(grid, colourmap):
    return ["".join(colourmap[row]) for row in grid]


def draw_grid(grid):
    print("\033[H\033[3J", end="")
    for row in grid:
        print(row, flush=True)

def main():
    just_fix_windows_console()  # Needed as otherwise ANSII Escape codes bug out.
    COLOURMAP = np.array([" ", "@"])
    grid = colourmap_grid(generate_initial_cells(), COLOURMAP)
    # ANSII escape character. Moves cursor to the top of the terminal and clears everything below cursor.
    draw_grid(grid)

main()