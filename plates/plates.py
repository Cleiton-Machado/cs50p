def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = start_letter(s)
    s = min_max(s)
    s = verificar_pontuacao(s)
    s = first_zero(s)
    s = middle_numbers(s)
    return s

def start_letter(s):
    for letter in s[0:2]:
        if letter.isalpha():
            continue
        else:
            return False
    return s

def min_max(plate):
    if isinstance(plate, str):
        if len(plate) < 2 or len(plate) > 6:
            return False
        else:
            return plate
    else:
        return False

def first_zero(plate):
    if isinstance(plate, str):
        teste = []
        for char in plate:
            if char.isdigit():
                teste.append(char)
        if not teste:
            return plate
        elif teste[0] == '0':
            return False
        return plate
    else:
        return False

def verificar_pontuacao(plate):
    if isinstance(plate, str):
        for letter in plate:
            if letter.isalnum():
                continue
            else:
                return False
        return plate
    return False

def middle_numbers(plate):
    if isinstance(plate, str):
        plate_split = []
        for char in plate:
            plate_split.append(char)

        # verifica se está no último caracter da lista, se estiver da o return
        for index, char in enumerate(plate_split):
            if index == len(plate_split) - 1:
                return plate
        # verifica se o caracter da lista é um número, se for verifica se
        # o que está na frente dele não é número, se não for retorna Falso
            if char.isdigit() and not plate_split[index + 1].isdigit():
                return False

    else:
        return False

main()