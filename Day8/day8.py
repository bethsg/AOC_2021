#In[0]
import pandas as pd
signals = pd.read_table("input8.txt", sep=' \\| | ', header=None, engine='python')
#In[1]
check_values = [2, 3, 4, 7]
part1 = 0
for outputs in signals.values[:,10:14]:
    for output in outputs:
        if len(output) in check_values:
            part1 += 1
print("Solution to part 1: ", part1)
#In[2]
running_running_total = 0
for entry in signals.values:
    for signal in entry:
        if len(signal) == 2:
            cf = list(signal)
        elif len(signal) == 4:
            bd = list(signal)
        elif len(signal) == 3:
            a = list(signal)
    a = [element for element in a if element not in bd]
    bd = [element for element in bd if element not in cf]
    eg = [element for element in 'abcdefg' if element not in cf+a+bd]
    #Consider this decrypting the substitution cipher. Please
    running_total = ''
    for codes in entry[10:14]:
        if len(codes) == 2:
            running_total += '1'
        elif len(codes) == 3:
            running_total += '7'
        elif len(codes) == 4:
            running_total += '4'
        elif len(codes) == 5:
            if cf[0] in codes and cf[1] in codes:
                running_total += '3'
            elif not(bd[0] in codes and bd[1] in codes):
                running_total += '2'
            else:
                running_total += '5'
        elif len(codes) == 6:
            if not(cf[0] in codes) or not(cf[1] in codes):
                running_total += '6'
            elif not(bd[0] in codes) or not(bd[1] in codes):
                running_total += '0'
            else:
                running_total += '9'
        else:
            running_total += '8'
    running_running_total += int(running_total)
print("Solution to part 2: ", running_running_total)

# %%
