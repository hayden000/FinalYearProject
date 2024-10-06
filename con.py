assignment = [[1, 2], [3]]
auths = [[1, 2, 3], [3, 4]]


def eligibility_checker(assignment, auths):
    """
    Tests if all jobs in the assignment are eligible based on the auths
    Args:
        assignment: The jobs that must be completed together
        auths: The auths that each job requires

    Returns:
    True if all jobs in the assignment are eligible, False otherwise
    """
    for i in range(0, len(assignment)):
        for j in range(0, len(auths)):
            if i == j:
                if not set(assignment[i]).issubset(set(auths[j])):
                    return False
    return True


print(eligibility_checker(assignment, auths))
