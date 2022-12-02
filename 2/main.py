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

lose_condition = {v: k for k, v in win_condition.items()}

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
    plays = [line
                .replace('A', 'Rock')
                .replace('B', 'Paper')
                .replace('C', 'Scissors')
                .replace('X', 'Rock')
                .replace('Y', 'Paper')
                .replace('Z', 'Scissors')
                .split(' ')
             for line in lines]

    plays_pt2 = [line
                .replace('A', 'Rock')
                .replace('B', 'Paper')
                .replace('C', 'Scissors')
                .replace('X', 'Lose')
                .replace('Y', 'Draw')
                .replace('Z', 'Win')
                .split(' ')
             for line in lines]

    return plays, plays_pt2


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


def play_round_pt2(play):
    opponent_play = play[0]
    match_fix = play[1]

    if match_fix == 'Win': # Win
        my_play = lose_condition[opponent_play]
        return 6 + bonus[my_play]
    elif match_fix == 'Lose':  # Lose
        my_play = win_condition[opponent_play]
        return 0 + bonus[my_play]
    else:  # Draw
        my_play = opponent_play
        return 3 + bonus[my_play]


if __name__ == '__main__':
    plays, plays_pt2 = process_input()

    round_points = [play_round(play) for play in plays]
    round_points_pt2 = [play_round_pt2(play) for play in plays_pt2]

    print(sum(round_points))
    print(sum(round_points_pt2))
