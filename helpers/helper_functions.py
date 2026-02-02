def _load_new_with_0(input_list: list, inner_size: int) -> None:
    """
    Loads in place

    Example:
    [[1, 2, 3, 4]] ->
    [[1, 2, 3, 4], [0, 0, 0, 0]]
    """

    current_size = len(input_list)
    input_list.append([0 for _ in range(inner_size)])


def is_monotonic(input_list: list) -> bool:
    """
    Returns true if list is monotonic
    
    :param input_list: Description
    :type input_list: list
    :return: Description
    :rtype: bool
    """
    return all(input_list[index] < input_list[index + 1] for index in range(len(input_list) - 1))