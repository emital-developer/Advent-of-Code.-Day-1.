from First_Day.day_1_part_2 import *
import unittest
from collections import defaultdict


class TestDay1Part2(unittest.TestCase):

    def test_find_numbers_indices(self):
        self.assertEqual(find_numbers_indices('zero one two three', 'zero'), [0])
        self.assertEqual(find_numbers_indices('zero zero two three', 'zero'), [0, 5])
        self.assertEqual(find_numbers_indices('one two three', 'four'), [])
        self.assertEqual(find_numbers_indices('123456789', '3'), [2])
        self.assertEqual(find_numbers_indices('123456789', '10'), [])

    def test_searching_words(self):
        line = "zero two five eight"
        result = searching_words(line)
        expected = defaultdict(list, {'zero': [0], 'two': [5], 'five': [9], 'eight': [14]})
        self.assertEqual(result, expected)

        line = "zero zero two"
        result = searching_words(line)
        expected = defaultdict(list, {'zero': [0, 5], 'two': [10]})
        self.assertEqual(result, expected)

        line = "seven seven"
        result = searching_words(line)
        expected = defaultdict(list, {'seven': [0, 6]})
        self.assertEqual(result, expected)

    def test_searching_numbers(self):
        line = "0123456789"
        result = searching_numbers(line)
        expected = defaultdict(list, {str(i): [i] for i in range(10)})
        self.assertEqual(result, expected)

        line = "123 456 789"
        result = searching_numbers(line)
        expected = defaultdict(list, {'1': [0], '2': [1], '3': [2], '4': [4], '5': [5], '6': [6], '7': [8], '8': [9],
                                      '9': [10]})
        self.assertEqual(result, expected)

        line = "no numbers here"
        result = searching_numbers(line)
        expected = defaultdict(list)
        self.assertEqual(result, expected)

    def test_sum_of_edge_numbers(self):
        data = ["zero one two three", "four five six seven", "eight nine zero one"]
        result = sum_of_edge_numbers(data)
        expected = 3 + 47 + 81  # edges: 1, 47, 81
        self.assertEqual(result, expected)

        data = ["zero zero two", "seven seven", "no numbers here"]
        result = sum_of_edge_numbers(data)
        expected = 2 + 77 + 0  # edges: 0, 77, 0
        self.assertEqual(result, expected)

        data = ["123 456 789", "012 345", "678 901"]
        result = sum_of_edge_numbers(data)
        expected = 19 + 5 + 61  # edges: 19, 5, 61
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
