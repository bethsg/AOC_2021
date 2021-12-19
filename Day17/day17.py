#In[0]
lx = 70
ux = 125
ly = -159
uy = -121
#Puzzle input

#In[1]
def ValidY(vel, pos):
    if pos >= ly and pos <= uy:
        return True
    elif pos < ly:
        return False
    else:
        return ValidY(vel-1, pos + vel)

valid_ys = []

for y in range(ly, 1000):
    if ValidY(y, 0):
        valid_ys.append(y)

max_y = max(valid_ys)
print("The highest vertical position the probe can reach whilst still being on targer is: ",(max_y*(max_y + 1))/2)

#In[2]
def ValidX(vel, pos):
    if pos >= lx and pos <= ux:
        return True
    elif pos > ux or vel == 0:
        return False
    else:
        return ValidX(vel-1, pos + vel)

valid_xs = []

for x in range(0, 1000):
    if ValidX(x, 0):
        valid_xs.append(x)

def ValidXY(xvel, xpos, yvel, ypos):
    if xpos >= lx and xpos <= ux and ypos >= ly and ypos <= uy:
        return 1
    elif xpos > ux or ypos < ly:
        return 0
    else:
        if xvel == 0:
            return ValidXY(0, xpos + xvel, yvel -1, ypos + yvel)
        else:
            return ValidXY(xvel -1, xpos + xvel, yvel -1, ypos + yvel)

count = 0
for y in valid_ys:
    for x in valid_xs:
        count += ValidXY(x, 0, y, 0)
print("Total unique initial velocities:", count)

# %%
