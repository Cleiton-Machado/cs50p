def main():
    time = input('What time is it? ')
    hora = convert(time)
    if hora >= 7 and hora <= 8:
        print('breakfast time')
    elif hora >= 12 and hora <= 13:
        print('lunch time')
    elif hora >= 18 and hora <=19:
        print('dinner time')

def convert(time):
    hora, minuto = time.split(':')
    minuto = round(int(minuto) * 1.66)
    tempo = (((int(hora)) * 100) + minuto) / 100
    return tempo


if __name__ == "__main__":
    main()