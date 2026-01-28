import random

def get_random_list(size=100):
    random_list = [x for x in range(1, size+1)]
    random.shuffle(random_list)
    return random_list


def get_randomized_lists(SIZE : int = 100, LIST_AMOUNT : int = 2**12) -> list[list[int]]:
    """
    Returns a list with lists inside of it with randomized values.
    Uses 'random' library.

    Inner lists are guaranteed to have 1 of every number from 1 to n where n is length of the list.
    """

    final_list = []

    for _ in range(LIST_AMOUNT):
        random_list = get_random_list(SIZE)
        final_list.append(random_list)
    
    return final_list