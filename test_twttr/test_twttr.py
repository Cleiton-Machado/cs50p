from twttr import shorten

def test_shorten():
    assert shorten('teste')  == 'tst'
    assert shorten('Cleiton') == 'Cltn'
    assert shorten('test.') == 'tst.'
    assert shorten('teste123') == 'tst123'
    assert shorten('TESTE') == 'TST'