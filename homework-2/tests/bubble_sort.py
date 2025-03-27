from main import bubble_sort
import pytest


@pytest.mark.parametrize("data, expected_result",
                         [
                             ([1, 1, 1, 1, 1, 2, 3, 4, 9, 0, 1, 1, 2, 3, 4, 5], [0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 9]),
                             ([300000000, 30, 1], [1, 30, 300000000])

                         ])

def test_bubble_sort_positive(data, expected_result):

    assert bubble_sort(data) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [
                             (None, TypeError),
                             ("123321", TypeError),
                             ("[1, 2, 3]", TypeError)
                         ])

def test_bubble_sort_negative(data, expected_result):

    with pytest.raises(expected_result):
        bubble_sort(data)


@pytest.mark.parametrize("data, expected_result",
                         [
                             ([-1, 1, 0.1], [-1, 0.1, 1]),
                             ([0], [0])
                         ])

def test_bubble_sort_borderline(data, expected_result):

    assert bubble_sort(data) == expected_result