#In[]
import numpy as np
fishies = np.loadtxt("input6.txt", int, delimiter=',')
fish_dick = {0:}

def Cycle(initial_fishies, days):
    next_gen = initial_fishies
    if days == 0:
        return next_gen
    else:
        for fish in range(0, len(initial_fishies)):
            if initial_fishies[fish] == 0:
                next_gen[fish] = 6
                next_gen = np.append(next_gen, 8)
            else:
                next_gen[fish] = next_gen[fish] - 1
        return Cycle(next_gen, days - 1)

#print("After 80 days, there would be", len(Cycle(fishies, 80))," lanternfish")
fishies = np.loadtxt("input6.txt", int, delimiter=',')
print("After 256 days, there would be", len(Cycle(fishies, 256))," lanternfish")

# %%
