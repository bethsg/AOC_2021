#In[0]
import numpy as np
chunks = np.loadtxt("input10.txt", str)

#In[1]
opens = ['[','{','(','<']
closes = [']','}',')','>']
points = [57, 1197, 3, 25137]
dictio = {}
dictio['x'] = 'plsnokeyerror'
pdictio = {}
sum_of_points = 0
for x in range(0, 4):
    dictio[opens[x]] = closes[x]
    pdictio[closes[x]] = points[x]

incomplete_lines = []
for x in range(0, len(chunks)):
    chunk = chunks[x]
    openers = ['x']
    for y in range(0, len(chunk)):
        chr = chunk[y]
        if chr in opens:
            openers = np.append(openers, chr)
        elif chr == dictio[openers[-1]]:
            openers = np.delete(openers, -1)
        else:
            sum_of_points += pdictio[chr]
            break
    else:
        openers = np.flip(np.delete(openers, 0))
        incomplete_lines = np.append(incomplete_lines, ''.join(openers))

print("Part 1: ", sum_of_points)

#In[2]
scores = []
newpdictio = {}
newpoints = [2,3,1,4]

for x in range(0, 4):
    newpdictio[opens[x]] = newpoints[x]
for line in incomplete_lines:
    score = 0
    for chr in line:
        score = (score * 5) + newpdictio[chr]
    scores = np.append(scores, score)

print("Part 2: ", np.median(np.sort(scores)))
