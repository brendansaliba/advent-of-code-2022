# Filename: main.py
# Created: 12/4/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description:


def process_input(PATH):
    file = open(PATH, 'r')
    lines = [line.rstrip() for line in file]
    return lines


def check_overlap(assignment):
    range_1, range_2 = split_ranges(assignment)
    return range_2[0] >= range_1[0] and range_2[1] <= range_1[1] or range_1[0] >= range_2[0] and range_1[1] <= range_2[1]


def check_parial_overlap(assignment):
    range_1, range_2 = split_ranges(assignment)
    return range_1[1] >= range_2[0] and range_2[1] >= range_1[0]


def split_ranges(assignment):
    assignment_pair = assignment.split(',')
    assignment_1 = assignment_pair[0].split('-')
    assignment_2 = assignment_pair[1].split('-')

    range_1 = [int(assignment_1[0]), int(assignment_1[1])]
    range_2 = [int(assignment_2[0]), int(assignment_2[1])]

    return range_1, range_2


if __name__ == '__main__':
    PATH = 'input.txt'
    assignments = process_input(PATH=PATH)

    truthers_real = [check_overlap(assignment) for assignment in assignments]
    print(sum(truthers_real))

    truthers_2 = [check_parial_overlap(assignment) for assignment in assignments]
    print(sum(truthers_2))
