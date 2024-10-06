from z3 import *

atMost = [[2, [5, 1, 9]]]
atLeast = [[2, [1, 2, 4, 3, 6, 7, 8]]]
auths = [[1, 2, 3, 4, 6], [2, 3, 4, 6, 5], [1, 4, 6, 7, 8, 9]]
sod = [[2, 4]]
bod = [[2, 3]]


def solve(atMost, atLeast, auths, sod, bod, numsteps, numusers):
    """
    A function that solves the WSP problem using z3 solver
    Args:
        atMost: The at most constraint
        atLeast: The at least constraint
        auths: The autharisation constraint
        sod: Steps to be completed by different users
        bod: Steps to be completed the same users
        numsteps: The number of steps
        numusers: The number of users
    Returns:
        A list of steps that are completed by the users (solution)
    """

    solveZ3 = z3.Solver()
    vars = {}
    # Setting up the variables
    for i in range(1, numsteps + 1):
        for j in range(1, numusers + 1):
            # Creation of the boolean variables for each step and user pair
            vars[(i, j)] = z3.Bool(str(i) + str(j))
    for i in range(1, numsteps + 1):
        # Enforce that each step is completed by at most one user and at least one user
        solveZ3.add(z3.Sum([z3.If(vars[(i, j)], 1, 0) for j in range(1, numusers + 1)]) == 1)
    for i in bod:
        # A step is completed by the same user using the implication fucntion
        step1, step2 = i
        for j in range(1, numusers + 1):
            solveZ3.add(z3.Implies(vars[(step1, j)], vars[(step2, j)]))

    for i in sod:
        # A step is completed by different users using the nand function
        step1, step2 = i
        for j in range(1, numusers + 1):
            solveZ3.add(z3.Or(z3.Not(vars[(step1, j)]), z3.Not(vars[(step2, j)])))

    for user, auth in enumerate(auths):
        # Loop through the auths and enforce that the user is not authorised for the steps then it should not be allocated
        for step in range(1, numsteps + 1):
            if step not in auth:
                solveZ3.add(vars[(step, user + 1)] == False)

    for i in atMost:
        # Implementing the at most constraint by using the sum function to ensure that the sum of the variables is less than the limit
        limit = i[0]
        constraints = i[1]
        for j in range(1, numusers + 1):
            temp = [vars[(k, j)] for k in constraints]
            solveZ3.add(z3.Sum(temp) <= limit)
    for i in atLeast:
        # Implementing the at least constraint by using the sum function to ensure that the sum of the variables is greater than the limit
        limit = i[0]
        constraints = i[1]
        for j in range(1, numusers + 1):
            temp = [vars[(k, j)] for k in constraints]
            solveZ3.add(z3.Sum(temp) >= limit)

    # print(solveZ3)
    # Out put the solution
    solution = []
    if solveZ3.check() == sat:
        model = solveZ3.model()
        for step in range(1, numsteps + 1):
            for user in range(1, numusers + 1):
                # Determine which steps are completed by which users by checking the model
                if model.eval(vars[step, user] == z3.BoolVal(True)):
                    solution.append([step, user])
        for i in solution:
            step, user = i
            # Shows the solution
            print("user: ", user, " ----> ", "step:", step)

    # print(model)
    solveZ3 = z3.Solver()


solve(atMost, atLeast, auths, sod, bod, numsteps=9, numusers=3)
