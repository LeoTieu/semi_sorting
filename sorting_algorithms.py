from helpers.helper_functions import _load_new_with_0


def bubble_sort_but_only_one_iteration(input_list: list):
    n = len(input_list)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
        break


def sort_all(sorting_function : callable, full_list: list[list[int]]):
    """Sorts many lists and returns a chart of the average values."""
    inner_size = len(full_list[0])
    amount_of_lists = len(full_list)

    time_chart_list = []
    _load_new_with_0(time_chart_list, inner_size)

    for inner_list in full_list:
        for index in range(inner_size):
            weighted_value = inner_list[index] / amount_of_lists
            time_chart_list[0][index] += weighted_value
    
    return time_chart_list