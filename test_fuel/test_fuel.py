from fuel import convert, gauge
import pytest

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert('5/1')

#def test_incorrect_int():
#    assert

def test_e_gauge():
    assert gauge(0) == 'E'

def test_e_gauge():
    assert gauge(1) == 'E'

def test_f_gauge():
    assert gauge(99) == 'F'

def test_percentage_gauge():
    assert gauge(75) == '75%'
