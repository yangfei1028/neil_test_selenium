#coding: utf-8

"""
@Author: Well
@Date: 2014-03-09
"""

#习题20: 函数和文件

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)

print ("Print the whole file: \n")
print_all(current_file)

print("Rewind, kind of like a tape")
rewind(current_file)
print("Print all lines")

current_line = 1
while current_line < len(current_file.readlines()):
    print_a_line(current_line, current_file)
    current_line += 1
    print current_line, len(current_file.readlines())





