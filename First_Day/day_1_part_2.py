from collections import defaultdict

dict_words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

numbers = '0123456789'


def find_numbers_indices(string, number):
    """Finding indices of each appearance of numeral substring"""
    indices = []
    index = -1
    while True:
        index = string.find(number, index + 1)
        if index == -1:
            break
        indices.append(index)
    return indices


def searching_words(line, d=None):
    """Searching for number words with indices and adding them to dictionary"""
    if not d:
        d = defaultdict(list)
    for number in dict_words:
        if number in line:
            indices = find_numbers_indices(line, number)
            d[number].extend(indices)
    return d


def searching_numbers(line, d=None):
    """Searching for numbers with indices and adding them to dictionary"""
    if not d:
        d = defaultdict(list)
    for number in numbers:
        if number in line:
            indices = find_numbers_indices(line, number)
            d[number].extend(indices)
    return d


def sum_of_edge_numbers(data):
    """Finding the edge numbers and summing them"""
    lst = []

    for line in data:
        d_w = searching_words(line)
        d_n = searching_numbers(line)
        idx_left, idx_right, left, right = '', '', '', ''
        min_index, max_index = len(line) - 1, 0

        if not d_w and not d_n:
            left, right = '0', '0'

        if d_w:  # Finding the left and right number words with indices
            for n in d_w:
                idx_left = min(d_w[n])
                if idx_left <= min_index:
                    min_index = idx_left
                    left = dict_words[n]

                idx_right = max(d_w[n])
                if idx_right >= max_index:
                    max_index = idx_right
                    right = dict_words[n]
        if d_n:  # Finding the left and right numbers with indices
            for n in d_n:
                idx_left = min(d_n[n])
                if idx_left <= min_index:
                    min_index = idx_left
                    left = n

                idx_right = max(d_n[n])
                if idx_right >= max_index:
                    max_index = idx_right
                    right = n

        lst.append(int(left + right))  # Adding the sum of the numbers to a list
    return sum(lst)  # Returning the sum of the numbers in the list


def main():
    with open('day_1_data.txt') as text:
        print(sum_of_edge_numbers(text))


if __name__ == "__main__":
    main()
