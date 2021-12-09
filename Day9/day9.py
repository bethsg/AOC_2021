#In[0]
import numpy as np
heightmap = np.loadtxt("input9.txt", str)
sum_of_risk_levels = 0
length = len(heightmap) - 1
width = len(heightmap[0]) - 1

def CheckAdj(ord_y, ord_x):
    if ord_y == 0:
        if ord_x == 0:
            if int(heightmap[0][0]) < int(heightmap[0][1]) and int(heightmap[0][0]) < int(heightmap[1][0]):
                return int(heightmap[0][0]) + 1, ()
        elif ord_x == width:
            if int(heightmap[0][width]) < int(heightmap[0][width - 1]) and int(heightmap[0][width]) < int(heightmap[1][width]):
                return int(heightmap[0][width]) + 1
        else:
            if int(heightmap[0][ord_x]) < int(heightmap[0][ord_x - 1]) and int(heightmap[0][ord_x]) < int(heightmap[0][ord_x + 1]) and int(heightmap[0][ord_x]) < int(heightmap[1][ord_x]):
                return int(heightmap[0][ord_x]) + 1
    elif ord_x == 0:
        if ord_y == length:
            if int(heightmap[length][0]) < int(heightmap[length - 1][0]) and int(heightmap[length][0]) < int(heightmap[length][1]):
                return int(heightmap[length][0]) + 1
        else:
            if int(heightmap[ord_y][0]) < int(heightmap[ord_y + 1][0]) and int(heightmap[ord_y][0]) < int(heightmap[ord_y - 1][0]) and int(heightmap[ord_y][0]) < int(heightmap[ord_y][1]):
                return int(heightmap[ord_y][0]) + 1
    elif ord_y == length:
        if ord_x == width:
            if int(heightmap[length][width]) < int(heightmap[length][width - 1])  and int(heightmap[length][width]) < int(heightmap[length - 1][width]):
                return int(heightmap[length][width]) + 1
        else:
            if int(heightmap[length][ord_x]) < int(heightmap[length][ord_x + 1]) and int(heightmap[length][ord_x]) < int(heightmap[length][ord_x -1]) and int(heightmap[length][ord_x]) < int(heightmap[length - 1][ord_x]):
                return int(heightmap[length][ord_x]) + 1
    elif ord_x == width:
        if int(heightmap[ord_y][width]) < int(heightmap[ord_y + 1][width]) and int(heightmap[ord_y][width]) < int(heightmap[ord_y - 1][width]) and int(heightmap[ord_y][width]) < int(heightmap[ord_y][width - 1]):
            return int(heightmap[ord_y][width]) + 1
    else:
        if int(heightmap[ord_y][ord_x]) < int(heightmap[ord_y + 1][ord_x]) and int(heightmap[ord_y][ord_x]) < int(heightmap[ord_y][ord_x + 1]) and int(heightmap[ord_y][ord_x]) < int(heightmap[ord_y][ord_x - 1]) and int(heightmap[ord_y][ord_x]) < int(heightmap[ord_y - 1][ord_x]):
            return int(heightmap[ord_y][ord_x]) + 1
    return 0

basin_dick = {}
for y in range(0, length + 1):
    for x in range(0, width + 1):
        risk_level = CheckAdj(y,x)
        sum_of_risk_levels += risk_level
        if risk_level > 0:
            basin_dick[(y,x)] = 'hey'

print("Sum of the risk leves: ", sum_of_risk_levels)
#In[1]
points_dick = {}
def FindBasin(inp):
    if int(heightmap[inp[0]][inp[1]]) == 9:
        return
    if inp in basin_dick.keys():
        if basin_dick[inp] == 'hey':
            if inp in points_dick:
                points_dick[inp] = points_dick[inp] + 1
            else:
                points_dick[inp] = 1
            return
        else:
            return FindBasin(basin_dick[inp])
    elif inp[0] > 0 and int(heightmap[inp[0] - 1][inp[1]]) < int(heightmap[inp[0]][inp[1]]):
        basin_dick[inp] = (inp[0]-1, inp[1])
    elif inp[0] < length and int(heightmap[inp[0] + 1][inp[1]]) < int(heightmap[inp[0]][inp[1]]):
        basin_dick[inp] = (inp[0]+1, inp[1])
    elif inp[1] > 0 and int(heightmap[inp[0]][inp[1] - 1]) < int(heightmap[inp[0]][inp[1]]):
        basin_dick[inp] = (inp[0], inp[1]-1)
    elif inp[1] < width and int(heightmap[inp[0]][inp[1] + 1]) < int(heightmap[inp[0]][inp[1]]):
        basin_dick[inp] = (inp[0], inp[1]+1)
    return FindBasin(basin_dick[inp])

for y in range(0, length + 1):
    for x in range(0, width + 1):
        FindBasin((y, x))

top_3 = np.prod(np.sort(list(points_dick.values()))[-3:])

print("Product of the size of the top 3 basins: ", top_3)
