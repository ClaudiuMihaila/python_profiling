from random import shuffle
from timeit import time_func

size = 2500

@time_func
def initialize_collection():
    items = [i for i in range(size)]
    shuffle(items)
    return items

@time_func
def find_indexes(items):
    indexes = [items.index(value) for value in range(size)]
    return indexes

@time_func
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






