import inflect

p = inflect.engine()

# In a file called adieu.py, implement a program that prompts the user for names,
#one per line, until the user inputs control-d.

nomes = []

while True:
    try:
        nome = input('Name: ')
    except EOFError:
        print(f'Adieu, adieu, to {nomes_tupla}')
        break

    nomes.append(nome)
    nomes_tupla = p.join(tuple(nomes))

