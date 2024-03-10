import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    lista = re.findall(r"\bum\b", s.lower())
    return len(lista)


if __name__ == "__main__":
    main()
