# Filename: main.py
# Created: 12/5/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description: HARDCODE CENTRAL

import re

class Boat:
    def __init__(self, crate_dict):
        self.crate_dict = crate_dict


    def rearrange(self, instruction):
        (quantity, origin, destination) = re.match(r"move (\d+) from (\d+) to (\d+)", instruction).groups()
        quantity, origin, destination = int(quantity), int(origin), int(destination)
        to_move = crate_dict[origin][-quantity:]
        # UNCOMMENT FOR PART 1
        # to_move.reverse()
        crate_dict[origin] = crate_dict[origin][: len(crate_dict[origin]) - quantity]
        crate_dict[destination].extend(to_move)


    def request_top_of_stack(self):
        tops = []
        for stack in crate_dict:
            # print(stack)
            # print(crate_dict[stack])
            tops.append(crate_dict[stack][-1])
        return tops

def process_input(PATH):
    file = open(PATH, 'r')
    lines = [line.rstrip() for line in file]

    columns_file = open('columns.txt', 'r')
    crates = [line.rstrip() for line in columns_file]

    return lines, crates


if __name__ == '__main__':
    PATH = 'input.txt'
    crate_indecies = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    index_map = {
        1: 1,
        5: 2,
        9: 3,
        13: 4,
        17: 5,
        21: 6,
        25: 7,
        29: 8,
        33: 9
    }
    crate_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    instructions, crates = process_input(PATH=PATH)

    for row in crates:
        for index in crate_indecies:
            if row[index].isalpha():
                crate_dict[index_map[index]].insert(0, row[index])

    boat = Boat(crate_dict=crate_dict)

    # print(boat.crate_dict)
    # boat.rearrange('move 2 from 7 to 2')
    # print(boat.crate_dict)
    # boat.rearrange('move 1 from 4 to 8')
    # print(boat.crate_dict)

    for instruction in instructions:
        boat.rearrange(instruction)

    print(boat.request_top_of_stack())