#In[]
import numpy as np
import pandas as pd
data = pd.read_table("input5.txt", sep=',| ->',header=None, engine='python')
vent_lines = data.values
size = np.amax(vent_lines) + 1

def GenerateDiagram(path_list, part2):
    grid = np.full((size,size), 0, int)
    for point in path_list:
        if point[0] == point[2]:
            if point[1] <= point[3]:
                for y in range(point[1], point[3] + 1):
                    grid[y][point[0]] = grid[y][point[0]] + 1
            else:
                for y in range(point[3], point[1] + 1):
                    grid[y][point[0]] = grid[y][point[0]] + 1
        elif point[1] == point[3]:
            if point[0] <= point[2]:
                for x in range(point[0], point[2] + 1):
                    grid[point[1]][x] = grid[point[1]][x] + 1
            else:
                for x in range(point[2], point[0] + 1):
                    grid[point[1]][x] = grid[point[1]][x] + 1
        if part2:
            if (point[0] < point[2]) & (point[1] < point[3]):
                for y in range(0, (point[2] - point[0]) + 1):
                    grid[point[1] + y][point[0] + y] = grid[point[1] + y][point[0] + y] + 1
            elif (point[0] > point[2]) & (point[1] < point[3]):
                for y in range(0, (point[0] - point[2]) + 1):
                    grid[point[1] + y][point[0] - y] = grid[point[1] + y][point[0] - y] + 1
            elif (point[0] < point[2]) & (point[1] > point[3]):
                for y in range(0, (point[2] - point[0]) + 1):
                    grid[point[1] - y][point[0] + y] = grid[point[1] - y][point[0] + y] + 1
            elif (point[0] > point[2]) & (point[1] > point[3]):
                for y in range(0, (point[0] - point[2]) + 1):
                    grid[point[1]-y][point[0]-y] = grid[point[1] - y][point[0] - y] + 1
    return grid

def CountIntersectingLines(grid):
    counter = 0
    for i in grid:
        for j in i:
            if j >= 2:
                counter += 1
    return counter

print("Part 1: There are ", CountIntersectingLines(GenerateDiagram(vent_lines, False)), " overlapping lines.")
print("Part 2: There are ", CountIntersectingLines(GenerateDiagram(vent_lines, True)), " overlapping lines.")

# %%
