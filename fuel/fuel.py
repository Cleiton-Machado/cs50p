def main():
    qnt_fuel = prompt_fraction()
    if qnt_fuel <= 1:
        print('E')
    elif qnt_fuel >= 99:
        print('F')
    else:
        print(f'{qnt_fuel}%')

def prompt_fraction():
    while True:
        user_prompt = input('Fraction: ')
        try:
            x, y = user_prompt.split('/')
            if int(x) > int(y) or int(y) == 0:
                continue
            else:
                fraction = (int(x) / int(y)) * 100
            return round(fraction)
        except (ValueError, ZeroDivisionError):
            pass


main()