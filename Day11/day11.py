#In[0]
import numpy as np
octopuses = np.empty((0,10), str)
for line in np.loadtxt("input11.txt", str):
    octopuses = np.append(octopuses, [list(line)], axis=0)
octopuses1 = octopuses.astype(int)
octopuses2 = octopuses.astype(int)
#In[1]
def DayCycle(octos, flashes, days_remaining):
    if days_remaining == 0:
        return flashes
    else:
        for y in range(len(octos)):
            for x in range(len(octos[y])):
                octos[y][x] += 1
        octos, flashes = FlashCade(octos, False, flashes)
        return DayCycle(octos,flashes,days_remaining - 1)

def FlashCade(octs, flash_flag, flash_count):
    for y in range(len(octs)):
            for x in range(len(octs[y])):
                adjacent = [(y-1, x), (y+1, x), (y, x-1), (y, x+1), (y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]
                if octs[y][x] > 9:
                    octs[y][x] = 0
                    flash_count += 1
                    flash_flag = True
                    for i, j in adjacent:
                        if i in range(len(octs)) and j in range(len(octs[y])):
                            if octs[i][j] > 0:
                                octs[i][j] += 1
    if flash_flag:
        return FlashCade(octs, False, flash_count)
    else:
        return (octs, flash_count)

print(DayCycle(octopuses1, 0, 100), "octopuses flash after 100 steps")
#In[3]
def SynchroStep(octi, days_passed):
    days_passed = days_passed + 1
    for y in range(len(octi)):
            for x in range(len(octi[y])):
                octi[y][x] += 1
    octi, flashes = FlashCade(octi, False, 0)
    if flashes == 100:
        return days_passed
    else:
        return SynchroStep(octi, days_passed)
print("After ", SynchroStep(octopuses2, 0), " steps, the flashes synchronise")
