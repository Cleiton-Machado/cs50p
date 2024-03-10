# implement a program that prompts the user for items, one per line, until the user inputs control-d
lista = dict()

while True:
    try:
        item = input()
        if item not in lista:
            lista[item] =  1
        else:
            lista[item] = lista[item] + 1

    except EOFError:
        print()
        lista_sorted = sorted(lista.items())
        for item in lista_sorted:
            print(item[1], item[0].upper())
        break

