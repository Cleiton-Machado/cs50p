from um import count


def test_count():
    assert count("instrumentality") == 0
    assert count("enterobacterium") == 0


def test_uppercase():
    assert count("Um thanks for the album.") == 1


def test_comma():
    assert count("Um, um,") == 2


def test_dot():
    assert count("um... um...") == 2
