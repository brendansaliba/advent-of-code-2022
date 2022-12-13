# Filename: main.py
# Created: 12/9/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description:


def process_input(PATH):
    file = open(PATH, 'r')
    lines = [[*line.rstrip()] for line in file]
    trees = [[int(tree) for tree in line] for line in lines]
    height = len(trees)
    width = len(trees[0])
    return trees, height, width


def extract_column(matrix, col):
    return [row[col] for row in matrix]


def extract_row(matrix, row):
    return matrix[row]


def split_row(row, tree_x):
    row_left = row[:tree_x]
    row_right = row[tree_x+1:]
    tree_height = row[tree_x]

    return row_left, row_right, tree_height


def split_col(col, tree_y):
    col_top = col[:tree_y]
    col_bottom = col[tree_y+1:]
    tree_height = col[tree_y]

    return col_top, col_bottom, tree_height


def is_visible(tree, row_left, row_right, col_top, col_bottom):
    if len(row_left) == 0 or len(row_right) == 0 or len(col_top) == 0 or len(col_bottom) == 0:
        return True
    if tree > max(row_left) or tree > max(row_right) or tree > max(col_top) or tree > max(col_bottom):
        return True
    return False


def calculate_scenic_score(tree, row_left, row_right, col_top, col_bottom):
    left_count = 0

    if len(row_left) > 0:
        for visible_tree in row_left[::-1]:
            left_count += 1
            if visible_tree >= tree:
                break

    right_count = 0
    if len(row_right) > 0:
        for visible_tree in row_right:
            right_count += 1
            if visible_tree >= tree:
                break

    top_count = 0
    if len(col_top) > 0:
        for visible_tree in col_top[::-1]:
            top_count += 1
            if visible_tree >= tree:
                break

    bottom_count = 0
    if len(col_bottom) > 0:
        for visible_tree in col_bottom:
            bottom_count += 1
            if visible_tree >= tree:
                break

    return left_count * right_count * top_count * bottom_count

# PATH = 'trees.txt'
PATH = 'trees.txt'
tree_grid, height, width = process_input(PATH)

# print(split_row([0, 2, 0, 0, 2], 0))

# print(tree_grid)

visible_or_not = []
scenic_scores = []

for tree_y, row in enumerate(tree_grid):
    for tree_x, tree in enumerate(row):
        col = extract_column(tree_grid, tree_x)

        row_left, row_right, _ = split_row(row, tree_x)
        col_top, col_bottom, _ = split_col(col, tree_y)
        scenic_score = calculate_scenic_score(tree, row_left, row_right, col_top, col_bottom)
        scenic_scores.append(scenic_score)

        if is_visible(tree, row_left, row_right, col_top, col_bottom):
            visible_or_not.append(True)

print(len(visible_or_not))
print(max(scenic_scores))