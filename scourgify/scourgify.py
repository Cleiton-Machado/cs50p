from tabulate import tabulate
import sys
import csv

try:
    command_line_argument = sys.argv[1]
    index = command_line_argument.rfind('.')
except IndexError:
    sys.exit('Too few command-line arguments')

if len(command_line_argument) < 3:
    sys.exit('Too few command-line arguments')

if command_line_argument[index:] != '.csv':
    sys.exit('Not a CSV file')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

students = []
output = []
try:
    with open(command_line_argument, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            split_name = row['name'].split(",")
            output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})

except FileNotFoundError:
    sys.exit('Could not read invalid_file.csv')

command_line_argument_2 = sys.argv[2]

with open(command_line_argument_2, 'w') as dict_file:
    writer = csv.DictWriter(dict_file, fieldnames=['first', 'last', 'house'])
    writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
    for row in output:
        writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})


