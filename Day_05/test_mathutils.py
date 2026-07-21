from mathutils import average, biggest, is_prime


def test_average_basics():
    assert average([10, 20, 30]) == 20.0
    assert average([-1, 0, 1]) == 0


def test_average_empty():
    assert average([]) == 0


def test_biggest_basics():

    assert biggest([24, 215, 642]) == 642


def test_biggest():
    assert biggest([11, 1111, 1111]) == 1111


def test_is_prime():
    assert is_prime(7)


def test_is_prime_not():
    assert not is_prime(1)
