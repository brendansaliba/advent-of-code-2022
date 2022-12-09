# Filename: main.py
# Created: 12/8/22
# Author: Brendan Saliba
# Copyright 2022, Brendan Saliba
# Description:


class Directory:
    def __init__(self, dir_name):
        self.name = dir_name
        self.files = {}
        self.directories = {}

    def mkdir(self, dir_name):
        if dir_name not in self.directories:
            new_dir = Directory(dir_name)
            self.directories[dir_name] = new_dir

    def touch(self, file_name, file_size):
        if file_name not in self.files:
            new_file = File(file_name, file_size)
            self.files[file_name] = new_file

    def ls(self):
        pass


class File:
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.size = file_size


def process_input(PATH):
    file = open(PATH, 'r')
    lines = [line.rstrip() for line in file]

    return lines


def change_path(command, wd):
    if command == '/':
        wd.clear()
    elif command == '..':
        wd.pop()
    else:
        wd.append(command)


def change_directory(path, current_dir):
    return current_dir.directories[path]


if __name__ == '__main__':
    PATH = 'test.txt'
    logs = process_input(PATH)
    file_system = Directory('/')
    file_system.mkdir('test')
    file_system.directories['test'].mkdir('another')
    print(list(file_system.directories.keys()))
    print(list(file_system.directories['test'].directories.keys()))
    current_dir = file_system

    wd = ['asdf']

    for path in wd:
        current_dir = change_directory(path, current_dir)

    change_path('/', wd)

    for line in logs:
        print(line)
        split_line = line.split()

        if split_line[0] == '$' and split_line[1] == 'cd':
            # cd
            if split_line[2] == '/':
                change_path('/')

            elif split_line[2] == '..':
                change_path('..')

            else:
                name = split_line[2]
                change_path(name)

            change_directory()
        elif split_line[0] == '$' and split_line[1] == 'ls':
            # print('List contents')
            pass
        elif split_line[0] == 'dir':
            dir_name = split_line[1]

            current_dir.mkdir(dir_name)

            # print(f'DIR: {name}')
            # mkdir
        else:
            size = split_line[0]
            name = split_line[1]
            # print(f'FILE: {name} with size {size}')
            # touch
