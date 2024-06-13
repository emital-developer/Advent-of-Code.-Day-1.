n = '123456789'


def sum_of_edge_numbers(data):
    """Create a container that will store the edge numbers and then sum them all"""
    lst = []

    for line in data:
        l, r = 0, -1
        first, second = 0, 0

        while True:
            if line[l] in n and not first:
                first = line[l]
            else:
                l += 1
            if line[r] in n and not second:
                second = line[r]
            else:
                r -= 1

            if first and second:
                break
        lst.append(int(first + second))
    return sum(lst)


with open('day_1_data.txt') as text:
    print(sum_of_edge_numbers(text))
