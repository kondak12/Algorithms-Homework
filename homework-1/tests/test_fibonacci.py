from main import fibonacci
import pytest


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, [0]),
                             (1, [0, 1]),
                             (2, [0, 1, 1]),
                             (3, [0, 1, 1, 2]),
                         ])

def test_fibonacci_positive(data, expected_result):

    assert fibonacci(data) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [
                             (None, TypeError),
                             ([0, 1, 1, 2], TypeError),
                             (1.12, TypeError),
                             (-1, ValueError)
                         ])

def test_fibonacci_negative(data, expected_result):

    with pytest.raises(expected_result):
        fibonacci(data)


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, [0])
                         ])

def test_fibonacci_borderline(data, expected_result):

    assert fibonacci(data) == expected_result