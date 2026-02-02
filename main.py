from list_generation import get_randomized_lists
from sorting_algorithms import bubble_sort_but_only_one_iteration, sort_all
from visuals import generate_heatmap
import os


if __name__ == '__main__':
    SIZE = 100
    LIST_AMOUNT = 2**12
    random_lists = get_randomized_lists(SIZE, LIST_AMOUNT)

    generate_heatmap(sort_all(bubble_sort_but_only_one_iteration, random_lists))



    # print(sort_all(bubble_sort_but_only_one_iteration, random_lists))
    # print("done")
