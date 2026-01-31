from list_generation import get_randomized_lists
from sorting_algorithms import bubble_sort_but_only_one_iteration
import os




def sort_all(sorting_function : callable, full_list: list[list[int]]):
    pass

if __name__ == '__main__':
    SIZE = 100
    LIST_AMOUNT = 2**12
    INNER_LIST_SIZE = 100
    random_lists = get_randomized_lists(SIZE, LIST_AMOUNT)


    print(sort_all(bubble_sort_but_only_one_iteration, random_lists))


    # print(sort_all(bubble_sort_but_only_one_iteration, random_lists))
    # print("done")
