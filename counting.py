def atMost(jobGroups, atMostCount, atMostList):
    """
    A constraint checker that checks the max counting constraint
    args
        jobGroups (list): a possible plan being checked
        atMostCount (int): the max number of users allowed to be assigned to group
        atMostList (list): the list of jobs subject to the constraint
    returns
        boolean: true iff the condition is met
    """
    assignments = []
    for i in atMostList:
        for j, group in enumerate(jobGroups):
            if i in group:
                assignments.append(j)
                break
    if len(set(assignments)) <= atMostCount:
        return True
    return False


def atLeast(jobGroups, atLeastCount, atLeastList):
    """
    A constraint checker that checks the min counting constraint
    args
        jobGroups (list): a possible plan being checked
        atLeastCount (int): the min number of users allowed to be assigned to group
        atLeastList (list): the list of jobs subject to the constraint
    returns
        boolean: true iff the condition is met
    """
    assignments = []
    for i in atLeastList:
        for j, group in enumerate(jobGroups):
            if i in group:
                assignments.append(j)
                break
    if len(set(assignments)) >= atLeastCount:
        return True
    return False


def checkAllCounting(jobGroups, atMostCounts, atMostLists, atLeastCounts, atLeastLists):
    """
    A wrapper loop that checks the condition for an entire assignment
    args
        jobGroups (list): a possible plan being checked
        atMostCount (int): the max number of users allowed to be assigned to group
        atMostList (list): the list of jobs subject to the constraint
        atLeastCount (int): the min number of users allowed to be assigned to group
        atLeastList (list): the list of jobs subject to the constraint
    returns
        boolean: true iff all the conditions are met
    """
    violate = False
    for i in range(0, len(atMostCounts)):
        if not atMost(jobGroups, atMostCounts[i], atMostLists[i]):
            violate = True
    for i in range(0, len(atLeastCounts)):
        if not atLeast(jobGroups, atLeastCounts[i], atLeastLists[i]):
            violate = True
    return not violate


jobGroups = [[1, 2], [3], [4, 5]]
atMostCounts = [3, 4]
atMostLists = [[1, 2, 3], [2, 3]]
atLeastCounts = [1, 2]
atLeastLists = [[4], [4, 5]]
print(checkAllCounting(jobGroups, atMostCounts, atMostLists, atLeastCounts, atLeastLists))
