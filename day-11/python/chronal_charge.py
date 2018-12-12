#!/usr/bin/env python

from cell import Cell

with open("input.txt", "r") as f:
    grid_serial_number = int(f.read())

grid_size = 300

grid = []


def get_grid(grid, x, y, size):
    """
    Get all the cells in a 3x3 square where x and y are the center points
    """
    cells = []

    # (x, y)        (x + 1, y)        (x + 2, y)
    # (x, y + 1)    (x + 1, y + 1)    (x + 2, y + 1)
    # (x, y + 2)    (x + 1, y + 2)    (x + 2, y + 2)
    coordinates_to_search = []

    for i in range(0, size):
        for j in range(0, size):
            coordinates_to_search.append((x + i, y + j))

    for coord in coordinates_to_search:
        try:
            if coord[0] < 1 or coord[1] < 1:
                return
            cells.append(grid[coord[1] - 1][coord[0] - 1])
        except IndexError:  # we are on edge
            return []

    return cells


for y in range(1, grid_size + 1):
    r = []
    for x in range(1, grid_size + 1):
        r.append(Cell(x, y))
    grid.append(r)


coordinates = {}

for row in grid:
    for cell in row:
        three_by_three = get_grid(grid, cell.x, cell.y, 3)
        powers = map(lambda x: x.calculate_power(grid_serial_number),
                        three_by_three)
        
        coordinates[cell] = sum(powers)

highest_power = sorted(coordinates.items(),
                       key=lambda x: x[1],
                       reverse=True)[0][0]

print(f"AoC part 1 answer: X: {highest_power.x} Y: {highest_power.y}")
