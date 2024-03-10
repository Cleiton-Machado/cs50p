def main():
    valor_coke = 50
    valor_inserido = 0
    while True:
        moeda = solicitar_moeda()
        if moeda == 5 or moeda == 10 or moeda == 25:
            valor_inserido += moeda
            #            print(valor_inserido)

            if valor_inserido < valor_coke:
                print(f"Amount Due: {valor_coke - valor_inserido}")
            else:
                print(f"Change Owed: {valor_inserido - valor_coke}")
                break
        else:
            print(f"Amount Due: {valor_coke - valor_inserido}")


# Solicitar que insira uma moeda
def solicitar_moeda():
    valor = input("Insert Coin: ")
    return int(valor)


main()
