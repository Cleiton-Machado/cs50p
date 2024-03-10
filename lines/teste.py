import sys


# implement a program that expects exactly one command-line argument, the name (or path) of a Python file

try:
    command_line_argument = sys.argv[1]
    index = command_line_argument.rfind('.')
except IndexError:
    print('Too few command-line arguments')
    sys.exit()

if command_line_argument[index:] != '.py':
    print('Not a Python file')
    sys.exit()

if len(sys.argv) > 2:
    print('Too many command-line arguments')
    sys.exit()

# outputs the number of lines of code in that file, excluding comments and blank lines.

with open(command_line_argument) as file:
    for line in file:
        print(line)



'''testanfp
ooddp
fsgsgd
gfsg'''
                    #jjjj