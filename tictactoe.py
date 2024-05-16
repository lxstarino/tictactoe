import random
import math
import os

grid = []

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_grid(size):
    if len(grid) > 0:
        grid.clear()

    for x in range(0, size * size):
        grid.append(" ")

    render_grid()

def render_grid():
    sqrt = int(math.sqrt(len(grid)))
    add = 0
    for x in range(0, sqrt):
        for x in range(0, sqrt):
            if x + 1 == sqrt:
                print(" |", grid[x + add], "|")
            else: 
                print(" |", grid[x + add], end="", flush = True)
        add += sqrt

def checkwinner():
    def all_equal(lst):
        return lst[0] != ' ' and all(x == lst[0] for x in lst)

    size =  int(math.sqrt(len(grid)))

    for row in range(size):
        if all_equal([grid[row * size + col] for col in range(size)]):
            return grid[row * size]

    for col in range(size):
        if all_equal([grid[row * size + col] for row in range(size)]):
            return grid[col]

    if all_equal([grid[i * size + i] for i in range(size)]):
        return grid[0]

    return False

def switchPlayers(player, symbols):
    clearConsole()
    render_grid()

    result = checkwinner()
    if result != False:
        print(f"{result} has won!")
        return

    if not " " in grid:
        print("Tie! no one won :(")
        return

    if player != "bot":
        column = input(f"Please provide a number from 1-{len(grid)}: ")

        if column.isdigit() and int(column) > 0 and int(column) < len(grid) + 1 and grid[int(column) - 1] == " ":
            grid[int(column) - 1] = symbols[0]
            switchPlayers("bot", [symbols[0], symbols[1]])    
        else:
            switchPlayers("human", [symbols[0], symbols[1]])    
    else: 
        rand_column = random.randint(0, len(grid) - 1)

        if grid[rand_column] != " ":
            switchPlayers("bot", [symbols[0], symbols[1]])  
        
        grid[rand_column] = symbols[1]
        switchPlayers("human", [symbols[0], symbols[1]])

running = True
inp = input("Wanna play tictactoe? (Y/N): ")

while running:
    if inp.lower() == "y" or inp.lower() == "yes":
        size = input("Which size should the grid have?: ")
        symbol = input("Which symbol u want to play? (X or O): ").upper()

        if size.isdigit() and int(size) > 0:
            if symbol == 'X' or symbol == 'O':
                create_grid(int(size))

                bot_symbol = "O"
                if symbol == "O":
                    bot_symbol = "X"

                switchPlayers(random.choice(["human",  "bot"]), [symbol, bot_symbol])
            else:
                print("Please enter a valid symbol (X or O)")
        else:
            print("Please enter a valid digit above 0")
    else: 
        print("Goodbye!")
        running = False




    