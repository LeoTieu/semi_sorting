def _load_new_with_0(input_list: list, inner_size: int) -> None:
    """
    Loads in place

    Example:
    [[1, 2, 3, 4]] ->
    [[1, 2, 3, 4], [0, 0, 0, 0]]
    """

    current_size = len(input_list)
    input_list.append([0 for _ in range(inner_size)])
