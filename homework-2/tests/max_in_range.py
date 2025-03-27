from main import max_in_range
import pytest


@pytest.mark.parametrize("data1, data2, data3, expected_result",
                         [
                             ([1, 2 ,3 ,4], 1, 2, (2, 1, 0))
                         ])

def test_max_in_range_positive(data1, data2, data3, expected_result):

    assert max_in_range(data1, data2, data3) == expected_result


@pytest.mark.parametrize("data1, data2, data3, expected_result",
                         [
                             (None, None, None, AttributeError),
                             (0.001, 0.1, ["[bla-bla-bla]"], TypeError),
                             (1, 1, None, AttributeError)
                         ])

def test_max_in_range_negative(data1, data2, data3, expected_result):

    with pytest.raises(expected_result):
        max_in_range(data1, data2, data3)


@pytest.mark.parametrize("data1, data2, data3, expected_result",
                         [
                             ([1], 0, 0, (1, 0, 0))
                         ])

def test_max_in_range_borderline(data1, data2, data3, expected_result):

    assert max_in_range(data1, data2, data3) == expected_result