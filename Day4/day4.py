#In[]
import numpy as np
from numpy.lib.function_base import append
drawn_numbers = np.loadtxt("input4.txt", int, delimiter=',', max_rows=1)
fresh_boards = np.loadtxt("input4.txt", int, skiprows=1)
#Seperately loading the first line (the list of numbers called)
#and the rest (the bingo boards)

def BingoGame(numbers_called, boards):
    dn_counter = 0
    winning_boards = np.empty((0,2), int)
    while len(winning_boards) < (len(boards) / 5):
        number = numbers_called[dn_counter]
        for z in range(0, int(len(boards) / 5)):
            if np.any(winning_boards[:, 0] == z):
                continue
            for y in range(0, 5):
                for x in range(0, 5):
                    if boards[(z * 5) + y][x] == number:
                        boards[(z * 5) + y][x] = -1
                        if (sum(boards[(z * 5) + y]) == -5):
                            winning_boards = np.append(winning_boards, np.array([[z, number]]), axis=0)
                        else:
                            i = 0
                            for j in range(0, 5):
                                i += boards[(z * 5) + j][x]
                            if i == -5:
                                winning_boards = np.append(winning_boards, np.array([[z, number]]), axis=0)
                        break
                else:
                    continue
                break
        dn_counter += 1
    return(boards, winning_boards)
#Returns the game state after every board has reached bingo, and a 2D array
#containing the the ordinal number of a board and the number it won on,
#in order of time to win.

def CalcScore(post_game_boards, board_no, end_number):
    sum_of_unmarked_nos = 0
    for a in range(board_no * 5, (board_no * 5) + 5):
        for b in range(0, 5):
            if post_game_boards[a][b] >=0:
                sum_of_unmarked_nos += post_game_boards[a][b]
    score = sum_of_unmarked_nos * end_number
    return score
#Calculates the score of a board when it wins

played_game, order_of_winners = BingoGame(drawn_numbers, fresh_boards)
print("The score of the first winning card:", CalcScore(played_game, order_of_winners[0][0], order_of_winners[0,1]))
print("The score of the last winning card:", CalcScore(played_game, order_of_winners[len(order_of_winners) - 1][0], order_of_winners[len(order_of_winners) - 1,1]))

# %%
