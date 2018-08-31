from random import shuffle
from timeit import time_func
size = 2500


def initialize_collection():
    items = [i for i in range(size)]
    shuffle(items)
    return items


def find_indexes(items):
    indexes = [items.index(value) for value in range(size)]
    return indexes


def write_results(indexes):
    with open("out.txt", "w") as file:
        for i in range(size):
            file.write("value {} at index {}\n".format(i, indexes[i]))
            file.flush()


@time_func
def main():
    x = initialize_collection()
    indexes = find_indexes(x)
    write_results(indexes)


main()






