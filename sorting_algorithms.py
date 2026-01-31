def bubble_sort_but_only_one_iteration(input_list: list):
    n = len(input_list)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
                swapped = True
        break