import sys


# implement a program that expects exactly one command-line argument, the name (or path) of a Python file

try:
    command_line_argument = sys.argv[1]
    index = command_line_argument.rfind('.')
except IndexError:
    sys.exit('Too few command-line arguments')

if command_line_argument[index:] != '.py':
    sys.exit('Not a Python file')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

# outputs the number of lines of code in that file, excluding comments and blank lines.
linhas_validas = []

try:
    with open(command_line_argument, 'r') as file:
        for line in file:
            if not line.lstrip().startswith('#') and line.strip():
                linhas_validas.append(line.strip())

except FileNotFoundError:
    sys.exit('File does not exist')

print(len(linhas_validas))