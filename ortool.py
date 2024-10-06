from ortools.sat.python import cp_model


def SATsolver(rules, auths):
    """
    Solve the WSP problem using the SAT solver
    Args:
        rules: The constraints of the problem including bod and sod
        auths: The autharisations of the users
    Returns:
        List: The solution of the problem
    """
    # Parse the data into the correct format and create the model
    steps = []
    bod = []
    sod = []
    newrules = []
    for i in rules:
        newrules.append([int(i[0]) - 1, int(i[1]) - 1, i[2]])
    rules = newrules
    newauths = []
    for i in auths:
        sublist = []
        for j in i:
            sublist.append(j - 1)
        newauths.append(sublist)
    auths = newauths
    # Compute the number of users and steps
    unique = set()
    for i in auths:
        unique.update(i)
    users = list(unique)
    for i in range(1, len(auths) + 1):
        steps.append(i)
    for i in rules:
        if i[2] == "BOD":
            bod.append([i[0], i[1]])
        elif i[2] == "SOD":
            sod.append([i[0], i[1]])
    # Creation of the model
    Model = cp_model.CpModel()
    # A variable for each user and step pair
    vars = {}
    for i in range(0, len(users)):
        for j in range(0, len(steps)):
            vars[(i, j)] = Model.NewBoolVar(str(users[i]) + str(steps[j]))
    # Ensuring that each user is assigned to exactly one step
    for i in range(0, len(steps)):
        Model.Add(sum(vars[(j, i)] for j in range(0, len(users))) == 1)
    # Unpacking the bod constraint and enforcing that each pair of steps is assigned to at most one user
    for i, j in bod:
        for k in range(0, len(users)):
            Model.Add(vars[(k, i)] == vars[(k, j)])
    # Unpacking the sod constraint and enforcing that each pair of steps is assigned to different users
    for i, j in sod:
        for k in range(0, len(users)):
            Model.Add(vars[(k, i)] + vars[(k, j)] <= 1)
    # Implemeting the auth constraint by enforcing that each user is assigned to a step that is in the auth list
    for step_value in range(0, len(steps)):
        for user in range(0, len(users)):
            if user not in auths[step_value]:
                Model.Add(vars[(user, step_value)] == 0)
    # Solve the model
    Solver = cp_model.CpSolver()
    Solver.Solve(Model)
    solution = []
    # if Solver==cp_model.OPTIMAL or Solver==cp_model.FEASIBLE:
    # Output the solution where each step is assigned to a user
    for i in range(0, len(steps)):
        for j in range(0, len(users)):
            if Solver.Value(vars[(j, i)]) == 1:
                print(steps[i], users[j])
                solution.append([steps[i], users[j] + 1])  # user step in list
    return solution
