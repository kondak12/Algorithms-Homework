from main import three_sum
import pytest


@pytest.mark.parametrize("data, expected_result",
                         [
                             ([1, -1, 2, -2, 0, 3, 4, 0], [[1, -1, 0], [1, -1, 0], [-1, -2, 3], [2, -2, 0], [2, -2, 0]]),
                             ([-1, 1, 0], [[-1, 1, 0]])

                         ])

def test_three_sum_positive(data, expected_result):

    assert three_sum(data) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [
                             (None, TypeError),
                             (0.001, TypeError),
                             (1, TypeError)
                         ])

def test_three_sum_negative(data, expected_result):

    with pytest.raises(expected_result):
        three_sum(data)


@pytest.mark.parametrize("data, expected_result",
                         [
                             ([0, 0, 0], [[0, 0, 0]]),
                             ([0], [])
                         ])

def test_three_sum_borderline(data, expected_result):

    assert three_sum(data) == expected_result