from seasons import check_date_birth


def test_check_date_birth():
    assert check_date_birth('1986-02-03') == (1986, 2, 3)
