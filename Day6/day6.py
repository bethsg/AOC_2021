#In[]
import numpy as np
def InitialiseFish():
    fishies = np.loadtxt("input6.txt", int, delimiter=',')
    fish_dick = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for fish in fishies:
        fish_dick[fish] = fish_dick[fish] + 1

def Cycle(initial_fishies, days):
    next_gen = {}
    if days == 0:
        return initial_fishies
    else:
        for x in range(0, 8):
            next_gen[x] = initial_fishies[x+1]
        next_gen[6] = next_gen[6] + initial_fishies[0]
        next_gen[8] = initial_fishies[0]
        return Cycle(next_gen, days - 1)
        
InitialiseFish()
print("After 80 days, there would be", sum(Cycle(fish_dick, 80).values()), " lanterfish")
InitialiseFish()
print("After 256 days, there would be", sum(Cycle(fish_dick, 256).values())," lanternfish")

# %%
