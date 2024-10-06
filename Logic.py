import autharisationCheck
import checkConstraints
import generatePartitions

# import solutionView
# import tkinter as tk

numjobs = 4
rules = [[3, 4, "SOD"], [1, 2, "BOD"]]
autharisations = [[1, 2], [1, 2], [3], [4]]


def main(rules, autharisations):
    """
    A main function that takes the rules and the autharisations and returns the solution
    Args:
        rules: the constraints
        autharisations: the autharisations which indictate the jobs that can be done by the users
    Returns:
        A solution if it exists, otherwise an emtpy list
    """
    solution = autharisationCheck.authCheck(autharisations, checkConstraints.checkAll(rules,
                                                                                      generatePartitions.generate_partitions(
                                                                                          len(autharisations))))

    print("numjobs: ", numjobs)
    print("rules ", rules)
    print("auth:", autharisations)
    print('solution ', solution)
    # solutionView.App(None , solution)
    return solution


if __name__ == "__main__":
    main(rules, autharisations)
