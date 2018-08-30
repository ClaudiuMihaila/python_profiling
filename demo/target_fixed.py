from random import shuffle
from timeit import time_func


size = 2500


def initialize_collection():
    items = [i for i in range(size)]
    shuffle(items)
    return items


def find_indexes(items):
    index_map = {items[i]: i for i in range(size)}
    indexes = [lookup(index_map, value) for value in range(size)]
    return indexes


def lookup(index_map, value):
    return index_map[value]


def write_results(indexes):
    with open("out.txt", "w") as file:
        for i in range(size):
            file.write("value {} at index {}\n".format(i, indexes[i]))


@time_func
def main():
    x = initialize_collection()
    indexes = find_indexes(x)
    write_results(indexes)


main()






