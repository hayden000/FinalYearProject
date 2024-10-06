def authCheck(autharisations, allocations):
    """
    Checks if the autharisations are valid for the given allocations
    Args:
        autharisations: The autharisations to check
        allocations: The allocations to check

    Returns:
    The valid allocations
    """
    output = []
    for i in range(0, len(allocations)):
        valid = True
        for j in range(0, len(allocations[i])):
            if not ((allocations[i][j]) in ((autharisations))):
                valid = False
        if valid:
            output.append(allocations[i])
    return output
