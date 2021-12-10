#In[0]
import numpy as np
chunks = np.loadtxt("input10.txt", str)

#In[1]
opens = ['[', '{', '(', '<']
closes = [']','}',')','>']
points = [57, 1197, 3, 25137]
dictio = {}
dictio['x'] = 'plsnokeyerror'
points_dic = {}
sum_of_points = 0
incomplete_lines = []

for x in range(0, 4):
    dictio[opens[x]] = closes[x]
    points_dic[closes[x]] = points[x]

for chunk in chunks:
    openers = ['x']
    for chr in chunk:
        if chr in opens:
            openers = np.append(openers, chr)
        elif chr == dictio[openers[-1]]:
            openers = np.delete(openers, -1)
        else:
            sum_of_points += points_dic[chr]
            break
    else:
        openers = np.flip(np.delete(openers, 0))
        incomplete_lines = np.append(incomplete_lines, ''.join(openers))

print("Part 1: ", sum_of_points)

#In[2]
scores = []
points_part2 = [2, 3, 1, 4]

for x in range(0, 4):
    points_dic[opens[x]] = points_part2[x]

for line in incomplete_lines:
    score = 0
    for chr in line:
        score = (score * 5) + points_dic[chr]
    scores = np.append(scores, score)

print("Part 2: ", np.median(np.sort(scores)))
