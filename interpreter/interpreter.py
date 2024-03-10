def main():
    entrada = receber_entrada()
    transformada = transformar(entrada)


# receber o input
def receber_entrada():
    entrada = input('Expression: ')
    return entrada

# transformar o input em variaveis
def transformar(expressao):
    x, y, z = expressao.split()
    x = int(x)
    z = int(z)
    resultado = 0
    if y == "+":
        resultado = x + z
    elif y =="-":
        resultado = x - z
    elif y == "*":
        resultado = x * z
    elif y == "/":
        resultado = x / z

    print(f'{resultado:.1f}')


main()