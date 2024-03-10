from tabulate import tabulate
import sys
import csv

try:
    command_line_argument = sys.argv[1]
    index = command_line_argument.rfind('.')
except IndexError:
    sys.exit('Too few command-line arguments')

if command_line_argument[index:] != '.csv':
    sys.exit('Not a CSV file')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

try:
    with open(command_line_argument, 'r') as csv_file:
        reader = csv.reader(csv_file)
        print(tabulate(reader, headers="firstrow", tablefmt='grid'))

except FileNotFoundError:
    sys.exit('File does not exist')