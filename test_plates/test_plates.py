from plates import is_valid

def test_is_valid():
    assert is_valid('CLE10') == True
    assert is_valid('PI3.14') == False
    assert is_valid('00cs50') == False
    assert is_valid('56') == False
    assert is_valid('d') == False
    assert is_valid('cdpppppp56') == False
    assert is_valid('cle0d') == False
    assert is_valid("CS50.,?!") == False





