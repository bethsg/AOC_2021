#In[0]
import numpy as np
points = np.loadtxt("input13.txt", int, delimiter=',', max_rows=983)
moves = np.loadtxt("input13.txt", str, skiprows=983)
moves = moves[:, 2]

paper = np.full((np.max(points[:, 1])+1, np.max(points[:, 0])+1), '.', str)
for point in points:
    paper[point[1]][point[0]] = 'X'
#In[1]
def Fold(pap, moves, times):
    papier = pap
    for i in range(0, times):
        move = moves[i]
        axis, index = move.split('=')
        index = int(index)
        if axis == "y":
            a = papier[:index, :]
            b = np.flipud(papier[(index + 1):, :])
            diff = len(a) - len(b)
            for x in range(0, len(a[0])):
                for y in range(0, len(b)):
                    if b[y][x] == "X":
                        a[y+diff][x] = "X"
        else:
            a = papier[:, :index]
            b = np.fliplr(papier[:, (index +1):])
            diff = len(a[0]) - len(b[0])
            for x in range(0, len(b[0])):
                for y in range(0, len(a)):
                    if b[y][x] == "X":
                        a[y][x + diff] = "X"
        papier = a
    return papier

def CountDots(paper, moves):
    counter = 0
    part1 = Fold(paper, moves, 1)
    for x in range(0, len(part1[0])):
        for y in range(0, len(part1)):
            if part1[y][x] == "X":
                counter += 1
    return counter

print("There are ", CountDots(paper, moves), " after the 1st fold")
print(Fold(paper, moves, len(moves)))

# %%
