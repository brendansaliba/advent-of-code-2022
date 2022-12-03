# Filename: main.py
# Created: 12/1/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description:


def process_input():
    PATH = 'input.txt'
    file = open(PATH, 'r')
    lines = [line.rstrip() for line in file]
    return lines


def check_compartments(pack):
    # returns a set of the common items in the pack compartments
    pack_size = len(pack)
    compartment_1, compartment_2 = pack[:pack_size // 2], pack[pack_size // 2:]

    common_items = set(compartment_1).intersection(compartment_2)

    return common_items


def group_packs(packs, N):
    group = [iter(packs)] * N
    grouped_packs = zip(*group)
    return list(grouped_packs)


def check_packs(packs):
    common_items = [check_compartments(pack) for pack in packs]
    priorities = [get_priority(str(items).strip('\'{}')) for items in common_items]
    return priorities


def check_groups(grouped_packs):
    common_items = []

    for group in grouped_packs:
        item_sets = [set(pack) for pack in list(group)]
        common = item_sets[0].intersection(*item_sets[1:])
        common_items.append(common)

    return common_items


def get_priority(char):
    if not char.isalpha():
        raise Exception('Character must be a letter')

    return ord(char) - 96 if 96 < ord(char) < 123 else ord(char) - 38


if __name__ == '__main__':
    # Part 1
    packs = process_input()
    priorities = check_packs(packs)
    print(sum(priorities))

    # Part 2
    grouped_packs = group_packs(packs, 3)
    common_items = check_groups(grouped_packs)
    common_priorities = [get_priority(str(items).strip('\'{}')) for items in common_items]
    print(sum(common_priorities))