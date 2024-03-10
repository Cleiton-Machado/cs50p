from numb3rs import validate

def main():
    test_format()
    test_range()


def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'7.8.3') == False
    assert validate(r'9.9') == False
    assert validate(r'1') == False


def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'100000.255.255.255') == False
    assert validate(r'255.255.500.255') == False

if __name__ == "__main__":
    main()