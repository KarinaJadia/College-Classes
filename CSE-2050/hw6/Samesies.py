def samesies(L1, L2):
    # Check if the lists have the same length, fails if not the same length
    if len(L1) != len(L2):
        return False
    # Convert the lists to sets to compare them since sets don't care about order
    set1 = set(L1)
    set2 = set(L2)
    return set1 == set2