#In[]
import numpy as np
from numpy.lib.function_base import append
diagnostics = np.loadtxt("input3.txt", str)
# %%
gamma = ''
epsilon = ''
for x in range(0, len(diagnostics[0])):
    zero  = 0
    one = 0
    for y in range(0, len(diagnostics)):
        if int(diagnostics[y][x]) == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
print(gamma, epsilon)
print(int(gamma, base=2)*int(epsilon, base=2))
# %%
def Bit_Criteria(numbers, ordinal_bit, mode):
    mcb = 0
    for no in numbers:
        if no[ordinal_bit] == '0':
            mcb += -1
        else:
            mcb += 1
        
    if mode == 'OGR':
        if mcb >= 0:
            return '1'
        else:
            return '0'
    elif mode == 'CSR':
        if mcb >= 0:
            return '0'
        else:
            return '1'
        

def LSR(remaining_numbers, ordinal_bit, mode):
    if len(remaining_numbers) == 1:
        return remaining_numbers[0]
    else:
        vaild_numbers = []
        bc = Bit_Criteria(remaining_numbers, ordinal_bit, mode)
        for number in remaining_numbers:
            if number[ordinal_bit] == bc:
                vaild_numbers = np.append(vaild_numbers, number)
        return LSR(vaild_numbers, ordinal_bit+1, mode)

# %%
ogr = LSR(diagnostics, 0, 'OGR')
csr = LSR(diagnostics, 0, 'CSR')
print(ogr, csr)
print(int(ogr, base=2)*int(csr, base=2))

# %%
