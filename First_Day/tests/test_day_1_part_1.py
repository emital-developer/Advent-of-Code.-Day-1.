import pytest

from First_Day.day_1_part_1 import sum_of_edge_numbers


def test_sum_of_edge_numbers_normal_cases():
    data = [
        '5fournqxkbzthree\n',
        'one6four4\n'
    ]
    assert sum_of_edge_numbers(data) == 119


def test_sum_of_edge_numbers_empty_data():
    data = []
    assert sum_of_edge_numbers(data) == 0


def test_sum_of_edge_numbers_single_line():
    data = ['1twothree4five\n']
    assert sum_of_edge_numbers(data) == 14


def test_sum_of_edge_numbers_multiple_lines():
    data = [
        '1twothree4five\n',
        'six7eightnine0\n'
    ]
    assert sum_of_edge_numbers(data) == 91


def test_sum_of_edge_numbers_negative_numbers():
    data = [
        'neg-4none-9\n',
        'pos3some-1\n'
    ]
    assert sum_of_edge_numbers(data) == 80


if __name__ == '__main__':
    pytest.main()
