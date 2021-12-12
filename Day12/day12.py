#In[0]
import numpy as np
cave_sys = np.loadtxt("input12.txt", str, delimiter='-')
#In[1]
paths = {}
for cave in cave_sys:
    if cave[0] in paths.keys():
        paths[cave[0]] = np.append(paths[cave[0]], cave[1])
    else:
        paths[cave[0]] = [cave[1]]
    if cave[1] in paths.keys():
        paths[cave[1]] = np.append(paths[cave[1]], cave[0])
    else:
        paths[cave[1]] = [cave[0]]

def Explore(current, explored):
    if current.islower():
        explored = np.append(explored, current)
    if current == "end":
        return 1
    elif all(elem in explored for elem in paths[current]):
        return 0
    else:
        return sum([Explore(option, explored) for option in paths[current] if not(option in explored)])

print("There are ", Explore("start", []), " paths through the caves with part 1's rules")

#In[2]
def Explore2(current, explored, flag):
    if current.islower():
        explored = np.append(explored, current)
    if current == "end":
        return 1
    elif all(elem in explored for elem in paths[current]):
        if flag:
            return 0
        else:
            return sum([Explore2(option, explored, True) for option in paths[current] if option != "start"])
    else:
        if flag:
            return sum([Explore2(option, explored, True) for option in paths[current] if not(option in explored)])
        else:
            return sum([Explore2(option, explored, False) for option in paths[current] if not(option in explored)]) + sum([Explore2(option, explored, True) for option in paths[current] if option in explored and option != "start"])

print("There are ", Explore2("start", [], False), " paths through the caves with part 2's rules")