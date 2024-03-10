# Pedir um nome em camelCasa
def main():
    camelCase = input("camelCase: ")
    nome = snake_case(camelCase)
    imprimir_lista(nome)
    print()


# transforma o parâmetro de camelCase para uma lista em snake_case
def snake_case(camelCase):
    snake_case_name = []
    for letter in camelCase:
        if letter.isupper():
            snake_case_name.append(f"_{letter.lower()}")
        else:
            snake_case_name.append(letter)
    return snake_case_name


# imprimir lista com todas as letras na mesma linha
def imprimir_lista(lista):
    for i in lista:
        print(i, end="")


main()
