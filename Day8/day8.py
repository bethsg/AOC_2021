#In[]
from numpy import sign
import pandas as pd
from pandas.io.pytables import AppendableFrameTable
signals = pd.read_table("input8.txt", sep=' \\| | ', header=None, engine='python')
# %%
check_values = [2, 3, 4, 7]
part1 = 0
for outputs in signals.values[:,10:14]:
    for output in outputs:
        if len(output) in check_values:
            part1 += 1
print("Solution to part 1: ", part1)
# %%
gods = {}
running_running_total = 0
for entry in signals.values:
    for signal in entry:
        if len(signal) == 2:
            gods['c'] = list(signal)
            gods['f'] = list(signal)
        elif len(signal) == 4:
            gods['b'] = list(signal)
            gods['d'] = list(signal)
        elif len(signal) == 3:
            gods['a'] = list(signal)
    gods['a'] = [element for element in gods['a'] if element not in gods['b']]
    gods['b'] = [element for element in gods['b'] if element not in gods['c']]
    gods['d'] = gods['b']
    gods['e'] = [element for element in 'abcdefg' if element not in gods['c']+gods['a']+gods['b']]
    gods['g'] = gods['e']
    running_total = ''
    
    for codes in entry[10:14]:
        if len(codes) == 2:
            running_total += '1'
        elif len(codes) == 3:
            running_total += '7'
        elif len(codes) == 4:
            running_total += '4'
        elif len(codes) == 5:
            if gods['c'][0] in codes and gods['c'][1] in codes:
                running_total += '3'
            elif not(gods['d'][0] in codes and gods['d'][1] in codes):
                running_total += '2'
            else:
                running_total += '5'
        elif len(codes) == 6:
            if not(gods['c'][0] in codes) or not(gods['c'][1] in codes):
                running_total += '6'
            elif not(gods['b'][0] in codes) or not(gods['b'][1] in codes):
                running_total += '0'
            else:
                running_total += '9'
        else:
            running_total += '8'
    running_running_total += int(running_total)
print("Part 2: ", running_running_total)

# %%
