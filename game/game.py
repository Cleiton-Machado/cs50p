import random

# Prompts the user for a level, If the user does not input a positive integer, the program should prompt again.
while True:
    level = input("Level: ")
    try:
        if int(level) > 0:
            break
        else:
            continue
    except:
        pass

# Randomly generates an integer between 1 and, inclusive, using the random module

resposta = random.randint(1, int(level))

# Prompts the user to guess that integer.
# If the guess is not a positive integer, the program should prompt the user again.
while True:
    guess = input("Guess: ")
    try:
        int(guess)
        if int(guess) < 0:
            continue
        if int(guess) < resposta:
            print("Too small!")
            continue
        elif int(guess) > resposta:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except:
        pass

# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
