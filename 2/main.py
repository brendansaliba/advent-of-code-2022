# Filename: main.py
# Created: 12/1/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description: Nutty Elves

# Win conditions
win_condition = {
    'Rock': 'Scissors',
    'Scissors': 'Paper',
    'Paper': 'Rock'
}

bonus = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}


def process_input():
    PATH = 'input.txt'
    file = open(PATH, 'r')

    lines = [line.rstrip() for line in file]

    # world's nuttiest list comprehension
    lines = [line
                .replace('A', 'Rock')
                .replace('B', 'Paper')
                .replace('C', 'Scissors')
                .replace('X', 'Rock')
                .replace('Y', 'Paper')
                .replace('Z', 'Scissors')
                .split(' ')
             for line in lines]

    return lines


def play_round(play):
    opponent_play = play[0]
    my_play = play[1]
    bonus_points = bonus[my_play]

    if win_condition[my_play] == opponent_play:  # I win
        return 6 + bonus_points
    elif my_play == opponent_play:  # We tie
        return 3 + bonus_points
    else:  # I lose
        return 0 + bonus_points


if __name__ == '__main__':
    lines = process_input()

    round_points = [play_round(line) for line in lines]

    print(sum(round_points))
