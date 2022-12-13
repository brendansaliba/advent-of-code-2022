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
            print(f'Directory {dir_name} created in {self.name}')

    def touch(self, file_name, file_size):
        if file_name not in self.files:
            new_file = File(file_name, file_size)
            self.files[file_name] = new_file
            print(f'File {file_name} created in {self.name}')

    def ls(self):
        print('Dir:', self.name)
        print('Directories:', list(self.directories.keys()))
        print('Files:', list(self.files.keys()))
        pass


class File:
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.size = file_size


def process_input(PATH):
    file = open(PATH, 'r')
    lines = [line.rstrip() for line in file]

    return lines


def change_path(command, working_path):
    if command == '/':
        working_path.clear()
    elif command == '..':
        working_path.pop()
    else:
        working_path.append(command)


def change_directory(path, root):
    wd = root
    # print(f'Current dir {wd.name}')
    for dir in path[1:]:
        wd = wd.directories[dir]

    # print(f'New dir: {wd.name}')
    return wd


def is_command(line):
    if line[0] == '$':
        return True
    return False

def process_command(command):
    split_command = command.split()
    if split_command[1] == 'cd':
        if split_command[2] == '/':
            return '/'
        if split_command[2] == '..':
            return '..'
        return f'{split_command[2]}'
    elif split_command[1] == 'ls':
        return 'ls'


if __name__ == '__main__':
    PATH = 'test.txt'
    logs = process_input(PATH)

    root = Directory(dir_name='/')
    working_path = []
    working_directory = root

    for line in logs:
        if is_command(line):
            print(process_command(line))


    # for line in logs:
    #     print(line)
    #     split_line = line.split()
    #     print(f'Working dir {working_directory.name}')
    #     if split_line[0] == '$' and split_line[1] == 'cd':
    #         # cd
    #         if split_line[2] == '/':
    #             change_path('/', working_path)
    #
    #         elif split_line[2] == '..':
    #             change_path('..', working_path)
    #
    #         else:
    #             name = split_line[2]
    #             change_path(name, working_path)
    #
    #         working_directory = change_directory(working_path, root)
    #         print(f'WORKING DIR: ',working_directory.name)
    #
    #     elif split_line[0] == '$' and split_line[1] == 'ls':
    #         # print('List contents')
    #         pass
    #     elif split_line[0] == 'dir':
    #         dir_name = split_line[1]
    #         working_directory.mkdir(dir_name)
    #
    #     else:
    #         size = split_line[0]
    #         name = split_line[1]
    #         working_directory.touch(name, size)
    #
    #     print('-'*10)
    # working_directory.ls()
