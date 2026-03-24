def solve_puzzle(list, index_pos = 0, storage = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""
    # 1) Base case: have you found a valid solution?
    if storage == None:
        storage = {}
    if index_pos == len(list) - 1:
        return True
    elif index_pos not in storage:
        storage[index_pos] = False
        step_size = list[index_pos]
    # 2) Find all valid next-steps
        right_index = (step_size + index_pos) % len(list)
        left_index = (index_pos - step_size) % len(list)
        return solve_puzzle(list, right_index, storage) or solve_puzzle(list, left_index, storage)
    else:
        return False