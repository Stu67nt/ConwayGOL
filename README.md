# Conway's Game of Life

This project is a simulation of the famous 0 player cell automata game Conway's Game of life! It can simulate the regular game as well as a special mode with extra sudden events to add randomness to the deterministic game.

---

## Features

- Custom number of generations simluated
- Customisation of weights
- Special Events which affect the spawn/death cycles
- Cells can have colours!
- Randomly generated Bombs!
- Grid Scales with terminal size

## Usage Tutorial
When you run the program you can either run it without configuring the settings or configure them in you want to customise the board a bit. Here is an explanation of all the settings.   
| Setting | Explanation |
|:-------:|:-----------:|
| Dead Cell Weight | Configures the chance of a cell initally spawning empty/dead. |
| Alive Cell Weight  | Configures the chance of a cell initally spawning alive. |
| Bomb Cell Weight  | Configures the chance of a cell initally spawning with a bomb. |
| Normal Gen Weight  | Configures the chance of no special event. |
| Famine Gen Weight | Configures the chance of Famine special event. |
| Love Gen Weight  | Configures the chance of Love special event. |

You will get to see the inital state of the board before you start. If you wish to reset the board enter the letter 'r' to do so. This is the last stage to change the grid size with an explanation of how ot do so below.

### Changing Resolution
To change the board size quickly you need to zoom out/in in the terminal and/or change the font size. To zoom in or out quickly in the Windows terminal hold CRTL+Scroll. 
  
## Build & Run
This program has only been tested to run on Windows 11 so I cannot guarantee function on other platforms however I do not believe there is any reason why it shouldn't work.
#### Windows

    pip install ConwayGameOfLife
    ConwayGameOfLife


## AI Usage
ChatGPT was used for this project for the inital menu.
