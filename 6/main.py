# Filename: main.py
# Created: 12/6/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description:


def process_input(PATH):
    file = open(PATH, 'r')
    lines = [line.rstrip() for line in file]

    return lines


def is_marker(marker, WINDOW):
    char_set = set(marker)
    return True if len(char_set) >= WINDOW else False


if __name__ == '__main__':
    PATH = 'signal.txt'
    signals = process_input(PATH)

    WINDOW = 14
    signal = signals[0]

    ## TEST
    # signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

    for i, char in enumerate(signal[WINDOW:]):
        index = i+WINDOW
        rolling_window = signal[index-WINDOW:index]
        if is_marker(rolling_window, WINDOW):
            print(f'MARKER FOUND after character {index}')
            break
