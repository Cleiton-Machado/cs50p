import sys

def main():
    while True:
        try:
            user_prompt = input('Fraction: ')
            fraction = convert(user_prompt)
        except (ZeroDivisionError, ValueError):
            continue
        break

    percentage = gauge(fraction)
    print(percentage)


def convert(fraction):
    while True:
        x, y = fraction.split('/')
        if int(y) == 0:
            raise ZeroDivisionError
        elif int(x) > int(y):
            raise ValueError
        else:
            fraction = (int(x) / int(y)) * 100
        return round(fraction)



def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
