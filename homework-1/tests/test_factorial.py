from main import factorial
import pytest


@pytest.mark.parametrize("data, expected_result",
                         [
                             (1, 1),
                             (2, 2),
                             (3, 6),
                             (4, 24),
                             (5, 120)
                         ])

def test_factorial_positive(data, expected_result):

    assert factorial(data) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [
                             (None, TypeError),
                             ("", TypeError),
                             (1.12, TypeError),
                             (-1, ValueError)
                         ])

def test_factorial_negative(data, expected_result):

    with pytest.raises(expected_result):
        factorial(data)


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, 1)
                         ])

def test_factorial_borderline(data, expected_result):

    assert factorial(data) == expected_result