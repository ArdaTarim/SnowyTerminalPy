import os
import random
import time

DELAY = 0.5
SNOW_DENSITY = 5

snowflakes = ["❋", "❇", "❄️", "❆", "."]

term = os.get_terminal_size()
columns = term.columns
rows = term.lines

grid = []

for _ in range(rows):
    grid.append([" "] * columns)


def render_grid():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("\033[?25l")

    output = ""

    for row in grid:
        output += "".join(row) + "\n"

    output = output.strip("\n")

    print(output, end="")


while True:

    row = []

    for _ in range(columns):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(" ")

    grid.insert(0, row)
    grid.pop()

    render_grid()

    time.sleep(DELAY)
