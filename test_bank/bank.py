def main():
    greeting = input('Greeting: ').strip()
    valor = value(greeting)
    print(f'${valor}')


def value(greeting):
    if 'hello' in greeting or 'HELLO' in greeting:
        return 0
    elif greeting[0] == "h" or greeting[0] == 'H':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
