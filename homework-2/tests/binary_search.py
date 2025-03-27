from main import binary_search
import pytest


@pytest.mark.parametrize("data1, data2, expected_result",
                         [
                             ([1, 2, 3], 2, 1),
                             ([300000000, 30, 1], 30, 1)

                         ])

def test_binary_search_positive(data1, data2, expected_result):

    assert binary_search(data1, data2) == expected_result


@pytest.mark.parametrize("data1, data2, expected_result",
                         [
                             (1, None, TypeError),
                             (123321, "123321", TypeError),
                         ])

def test_binary_search_negative(data1, data2, expected_result):

    with pytest.raises(expected_result):
        binary_search(data1, data2)


@pytest.mark.parametrize("data1, data2, expected_result",
                         [
                             ([0, 0, 1], 0, 1),
                             ([1, 1, 1], 1, 1),
                             ([1, 0, 1], 1, 1)
                         ])

def test_binary_search_borderline(data1, data2, expected_result):

    assert binary_search(data1, data2) == expected_result