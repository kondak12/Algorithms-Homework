from main import count_ones
import pytest


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, 0),
                             (2, 1),
                             (5, 2)
                         ])

def test_count_ones_positive(data, expected_result):

    assert count_ones(data) == expected_result


@pytest.mark.parametrize("data, expected_result",
                         [
                             (None, TypeError),
                             ("123", TypeError),
                             (1.12, TypeError),
                             (-1, ValueError)
                         ])

def test_count_ones_negative(data, expected_result):

    with pytest.raises(expected_result):
        count_ones(data)


@pytest.mark.parametrize("data, expected_result",
                         [
                             (0, 0)
                         ])

def test_count_ones_borderline(data, expected_result):

    assert count_ones(data) == expected_result