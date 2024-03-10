from working import convert


def test_convert():
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"


def test_error_convert():
    with pytest.raises(ValueError):
        convert("8:00 PM 8:00 AM")
