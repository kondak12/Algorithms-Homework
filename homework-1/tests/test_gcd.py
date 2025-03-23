from main import gcd
import pytest


@pytest.mark.parametrize("data1, data2, expected_result",
                         [
                             (1, 3, 1),
                             (3, 9, 3),
                             (7, 49, 7)
                         ])

def test_gcd_positive(data1, data2, expected_result):

    assert gcd(data1, data2) == expected_result


@pytest.mark.parametrize("data1, data2, expected_result",
                         [
                             (1, None, TypeError),
                             (123321, "123321", TypeError),
                             (1.111, 1.11, TypeError)
                         ])

def test_gcd_negative(data1, data2, expected_result):

    with pytest.raises(expected_result):
        gcd(data1, data2)


@pytest.mark.parametrize("data1, data2, expected_result",
                         [
                             (0, 0, 0),
                             (1, 1, 1)
                         ])

def test_gcd_borderline(data1, data2, expected_result):

    assert gcd(data1, data2) == expected_result