from list_generation import get_randomized_lists
from sorting_algorithms import bubble_sort_but_only_one_iteration, sort_all
import os


if __name__ == '__main__':
    SIZE = 20
    LIST_AMOUNT = 2**12
    random_lists = get_randomized_lists(SIZE, LIST_AMOUNT)

    print(sort_all(bubble_sort_but_only_one_iteration, random_lists))



    # print(sort_all(bubble_sort_but_only_one_iteration, random_lists))
    # print("done")
