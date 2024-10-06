def checkBOD(job1, job2, jobGroups):
    """
    Checks if two jobs are assigned to the same person within a list of job groups.

    This function iterates through the list of job groups to determine if both the job1 and job2 are allocated to the same person.

    args
        job1 (int): the first job to check
        job2 (int): the second job to check
        jobGroups (list): a list of jobs where each group is represented as a list of job assignments

    returns
        bool: true when both jobs are assigned to the same person otherwise returns false
    """
    for group in jobGroups:
        if set([job1, job2]).issubset(set(group)):
            return True
    return False


def checkSOD(job1, job2, jobGroups):
    """
    Checks if two jobs are assigned to different people within a list of job groups.

    This function iterates through the list of job groups to determine if both the job1 and job2 are allocated to disparate users.

    args
        job1 (int): the first job to check
        job2 (int): the second job to check
        jobGroups (list): a list of jobs where each group is represented as a list of job assignments

    returns
        bool: true when both jobs are assigned to different people otherwise returns false
    """
    for group in jobGroups:
        if set([job1, job2]).issubset(set(group)):
            return False
    return True


def check(job1, job2, jobGroups, type):
    """
    A wrapper function that for the Check BOD and Check SOD functions

    This function calls the relevant constraint checker depending on if it is required to check BOD or SOD constraints

    args
        job1 (int): the first job to check
        job2 (int): the second job to check
        jobGroups (list): a list of jobs where each group is represented as a list of job assignments
        type (string): BOD for binding of duty and SOD for separation of duty
    returns
        bool: passes up the result of the constraint checker if it is of valid type
    """
    if type.upper() == "BOD":
        return checkBOD(job1, job2, jobGroups)
    elif type.upper() == "SOD":
        return checkSOD(job1, job2, jobGroups)
    print("invalid type")  # create exception error (error handling)


def checkAll(rules, allocation):
    """
    A loop wrapper function to loop through a plan and passed to the constraint checker and then to the relevant constraint checker

    args
        rules (list): a list where each element is a constraint
        allocation (list of lists): a list containing all allocations to check where each element is an allocation
    returns
        list: the list of valid assignments based on the rules list (constraints)
    """
    valid = []
    for i in allocation:
        satisfy = True
        for j in rules:
            if not check(j[0], j[1], i, j[2]):
                satisfy = False
        if satisfy:
            valid.append(i)
    if len(valid) == 0:
        print("error")
        return []
    else:
        return valid
