def checkBOD(job1, job2, jobGroups):
    """
    Checks if two jobs are in the same group
    Args:
        job1: job 1
        job2: job 2
        jobGroups: list of job groups
    Returns:
    If the jobs are in the same group
    """
    for group in jobGroups:
        if set([job1, job2]).issubset(set(group)):
            print([job1, job2])
            return True
    return False


test = [[3, 0], [2, 1]]
