from bank import value

def test_value_hello():
    assert value('hello') == 0

def test_value_h():
    assert value('hotel') == 20

def test_value_other():
    assert value('Bom dia') == 100
    assert value('Olá') == 100


def test_value_case_insentitivity():
    assert value('BOM DIA') == 100
    assert value('HELLO') == 0
    assert value('HOTEL') == 20
    assert value('BOM DIA') == 100
    assert value('BOA NOITE') == 100