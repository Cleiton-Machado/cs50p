entrees = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# implement a program that enables a user to place an order, prompting them for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).

def main():
    valor_pedido = 0
    while True:
        pedido = take_order()
        if pedido == '_parar_':
            print()
            break
        try:
            valor_pedido += return_valor(pedido)
        except TypeError:
            pass
        if valor_pedido == 0:
            continue
        print(f'${valor_pedido:.2f}')


def take_order():
    try:
        return input('Item: ').title()
    except EOFError:
        return '_parar_'

def return_valor(item):
    try:
        valor = entrees.get(item)
        return valor
    except TypeError:
        return None



main()