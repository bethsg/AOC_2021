#In[]
import numpy as np
drawn_numbers = np.loadtxt("input4.txt", int, delimiter=',', max_rows=1)
bingo_boards = np.loadtxt("input4.txt", int, skiprows=1)
print(len(bingo_boards))
#In[]
bingo_flag = False
dn_counter = 0
winning_board = -1
while not(bingo_flag):
    number = drawn_numbers[dn_counter]
    print(number)
    for z in range(0, int(len(bingo_boards)/5)):
        for y in range(0, 5):
            for x in range(0, 5):
                if bingo_boards[(z*5)+y][x] == number:
                    bingo_boards[(z*5)+y][x] = -1
                    if (sum(bingo_boards[(z*5)+y]) == -5):
                        bingo_flag = True
                        winning_board = z
                    else:
                        i = 0
                        for j in range(0, 5):
                            i += bingo_boards[(z*5)+j][x]
                        if i == -5:
                            bingo_flag = True
                            winning_board = z
                    break
            else:
                continue
            break
    dn_counter += 1
print(winning_board)
#In[]
print(2+2)


# %%
