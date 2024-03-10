import random


def main():
    level = get_level()
    acertos = 0
    for i in range(10):
        erros = 0
        x = generate_integer(level)
        y = generate_integer(level)
        question = f"{x} + {y} = "
        resposta_certa = x + y
        print(question, end="")
        while True:
            try:
                resposta_usuario = int(input(""))
                if resposta_usuario == resposta_certa:
                    acertos += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                erros += 1
                print("EEE")
                if erros == 3:
                    print(f"{question}{resposta_certa}")
                    break
                else:
                    print(question, end="")
                    acertos -= 1
    print(f"Score: {acertos}")


# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is
# a non-negative integer with
# digits. No need to support operations other than addition (+).


# Prompts the user for a level,
# If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [
                1,
                2,
                3,
            ]:
                return level
        except EOFError:
            print()
            exit()
        except:
            pass


# generate_integer returns a randomly generated non-negative integer with level digits
#  or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    else:
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
