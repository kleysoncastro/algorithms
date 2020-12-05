from insertion.insertion import insertion


def test_insertion():

    vec = [5, 2, 1, 6, 9]
    insertion(vec)
    assert vec == [1, 3, 5, 6, 9]
