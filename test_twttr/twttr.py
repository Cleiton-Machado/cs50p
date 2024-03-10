def main():
    # receber o texto do usuário
    texto = input('Input: ')

    print(shorten(texto))


def shorten(word):
    # converter o texto
    word_altered = []
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            continue
        else:
            word_altered.append(letter)
    return ''.join(word_altered)


if __name__ == "__main__":
    main()





