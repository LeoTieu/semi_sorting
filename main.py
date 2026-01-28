from list_generation import get_randomized_lists
import os

def bubble_sort_but_only_one_iteration(input_list: list):
    n = len(input_list)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
        break


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
