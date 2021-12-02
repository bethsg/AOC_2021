#In[]
import numpy as np
depth_report = np.loadtxt("input.txt")
increases = 0
#In[]
for point in range(1, len(depth_report)):
    if depth_report[point] > depth_report[point-1]:
        increases += 1
print(increases)
#In[]
increases2 = 0
for point in range(1, len(depth_report)-2):
    if int(sum(depth_report[point:point+3])) > int(sum(depth_report[point-1:point+2])):
        increases2 += 1
print(increases2)
#In[]
print(len(depth_report))
# %%
