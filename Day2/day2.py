#In[]
import numpy as np
sub_moves = np.loadtxt("input2.txt", str)
# %%
horizontal = 0
depth = 0
for move in sub_moves:
    if move[0] == 'forward':
        horizontal += int(move[1])
    elif move[0] == 'up':
        depth += -int(move[1])
    else:
        depth += int(move[1])
print(depth, horizontal, depth * horizontal)
# %%
hori2 = 0
depth2 = 0
aim = 0
for move in sub_moves:
    if move[0] == 'forward':
        hori2 += int(move[1])
        depth2 += aim * int(move[1])
    elif move[0] == 'up':
        aim += -int(move[1])
    else:
        aim += int(move[1])
print(depth2, hori2, depth2 * hori2)
# %%
