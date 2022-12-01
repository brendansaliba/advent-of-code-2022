# Filename: main.py
# Created: 12/1/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description:

def process_input():
    PATH = '/Users/brendansaliba/Projects/Advent of Code 2022/1/input.txt'
    file = open(PATH, 'r')

    lines = [line.rstrip() for line in file]

    return lines


if __name__ == '__main__':
    lines = process_input()
    calories_carried = []

    running = 0

    for line in lines:
        if line != '':
            calories = int(line)
            running += calories
        else:
            calories_carried.append(running)
            running = 0

    calories_carried = sorted(calories_carried, reverse=True)

    print(sum(calories_carried[0:3]))
