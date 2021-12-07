#In[]
import numpy as np
crab_moves = np.loadtxt("input7.txt", int, delimiter=',')
#In[]
limit = np.amax(crab_moves)
def UnioniseTheCrabs(mode):
    fuel_costs = []
    for x in range(0, limit + 1):
        running_cost = 0
        for move in crab_moves:
            if mode:
                temp =  abs(x - move)
                running_cost += (temp*(temp + 1)) / 2
            else:
                running_cost +=  abs(x - move)
        fuel_costs = np.append(fuel_costs, running_cost)
    return np.amin(fuel_costs)
    
print("Part 1: The cheapest outcome is: ", UnioniseTheCrabs(False))
print("Part 2: The cheapest outcome is: ", UnioniseTheCrabs(True))
# %%
