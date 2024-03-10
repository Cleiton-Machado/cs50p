from validator_collection import validators, checkers, errors


def main():
    email = input("What's your email address? ")
    print(validated(email))


def validated(email):
    try:
        email_address = validators.email(email)
        if email_address == email:
            return 'Valid'
    # Will raise an EmptyValueError
    except errors.EmptyValueError:
        return 'Invalid'
    # Handling logic goes here
    except errors.InvalidEmailError:
        return 'Invalid'



if __name__ == "__main__":
    main()
