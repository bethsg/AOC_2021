#In[0]
import numpy as np
from collections import defaultdict
from copy import copy
template = str(np.loadtxt("input14.txt", str, max_rows=1))
pairs = np.loadtxt("input14.txt", str, delimiter=" -> ", skiprows=1)

dick_pair = {}
cursed = defaultdict(int)
count = defaultdict(int)
for pair in pairs:
    dick_pair[pair[0]] = pair[1]
for x in range(0, len(template) - 1):
    count[template[x]] += 1
    adj = template[x] + template[x + 1]
    if adj in dick_pair.keys():
        cursed[adj] += 1
count[template[-1]] += 1

#In[1]
def BetterStep(cursed, count, steps):
    if steps == 0:
        return count
    else:
        temp = copy(cursed)
        for key, value in cursed.items():
            if value >= 1:
                count[dick_pair[key]] += value
                temp[key] = temp[key] - value
                if key[0] + dick_pair[key] in dick_pair.keys():
                    temp[key[0] + dick_pair[key]] += value
                if dick_pair[key] + key[1] in dick_pair.keys():
                    temp[dick_pair[key] + key[1]] += value
        return BetterStep(temp, count, steps - 1)
#In[2]
cursed1 = copy(cursed)
count1 = copy(count)
cursed2 = copy(cursed)
count2 = copy(count)
part_1  = BetterStep(cursed1, count1, 10)
print(max(part_1.values()) - min(part_1.values()))
part_2  = BetterStep(cursed2, count2, 40)
print(max(part_2.values()) - min(part_2.values()))

# %%
