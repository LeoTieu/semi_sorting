from list_generation import get_randomized_lists
from sorting_algorithms import bubble_sort_but_only_one_iteration
import os




if __name__ == '__main__':
    SIZE = 100
    LIST_AMOUNT = 2**12
    INNER_LIST_SIZE = 100
    random_lists = get_randomized_lists(SIZE, LIST_AMOUNT)


    for inner_list in random_lists:
        for _ in range(1):
            bubble_sort_but_only_one_iteration(inner_list)
    
    temp_array = [0.0 for _ in range(SIZE)]
    for index in range(SIZE):
        for inner_list in random_lists:
            temp_array[index] += (inner_list[index]/LIST_AMOUNT)

    print(temp_array)
