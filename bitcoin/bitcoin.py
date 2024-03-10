import sys
import requests

# Expects the user to specify as a command-line argument the number of Bitcoins, n,
# that they would like to buy. If that argument cannot be converted to a float,
# the program should exit via sys.exit with an error message.


def main():
    try:
        prompt = sys.argv[1]
    except:
        print("Missing command-line argument")
        sys.exit(1)

    prompt_float = converter_float(prompt)
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except:
        print('Erro ao efetor o Request')
        sys.exit(1)

    json_dict = r.json()
    rate = json_dict["bpi"]["USD"]["rate_float"]
    amount = rate * prompt_float
    print(f"${amount:,.4f}")


def converter_float(string):
    try:
        return float(string)

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


main()
