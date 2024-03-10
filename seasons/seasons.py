from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    date_birth = input('Date of Birth: ')

    year, month, day = check_date_birth(date_birth)


    date_of_birth = date(year, month, day)
    date_of_today = date.today()
    difference = date_of_today - date_of_birth
    total_minutes = difference.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + ' minutes')

def check_date_birth(date_birth):
    padrao = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(padrao, date_birth):
        year, month, day = date_birth.split('-')
        return int(year), int(month), int(day)
    else:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()