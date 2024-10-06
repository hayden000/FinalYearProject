import gurobipy


def model_wsp(steps, users, bod, sod, auths):
    """
    A linera programming model for the WSP problem.
    Args:
        steps: A list with the steps.
        users: A list with the users.
        bod: the list containing pairs of jobs that must be completed together.
        sod the list containing pairs of jobs that must be completed by different users.
        auths: the list containing the list of users that can be assigned to a job.
    Returns:
        Tuple: A dictionary with the assignment of the jobs to the users.
    """
    model = gurobipy.Model("wsp")
    variables = {}
    for i in steps:
        for j in users:
            name = str(i) + str(j)
            variables[i, j] = model.addVar(vtype=gurobipy.GRB.BINARY, name=name)
    objective = gurobipy.LinExpr()

    for i in bod:
        """
        Unpacking the list of pairs of jobs that must be completed together. And adding the constraint to the model.
        """
        step1, step2 = i
        for j in users:
            objective += (variables[step1, j] + variables[step2, j])
    for i in sod:
        """
        Unpacking the list of pairs of jobs that must be completed separately. And adding the constraint to the model.
        """
        step1, step2 = i
        for j in users:
            objective += (variables[step1, j] - variables[step2, j])

    """
    Ensure that all jobs are assigned to a user.
    """
    for index, user in enumerate(auths):
        for i in user:
            objective += variables[index + 1, i]
    for i in steps:
        constraints = gurobipy.LinExpr()
        for j in users:
            constraints += variables[i, j]
        model.addConstr(constraints == 1, name="all assigned")
    """
    Imposing the constraint that each job is assigned to 1 user.
    """
    for i in steps:
        constraints = gurobipy.LinExpr()
        for j in users:
            constraints += variables[i, j]
        model.addConstr(constraints <= 1, name="1 job 1 user")
    # Set the objective function to maximise the number of jobs assigned to users based on the value of the constraints.
    model.setObjective(objective, gurobipy.GRB.MAXIMIZE)
    status = model.optimize()
    assignment = {}
    # if model.Status == (GRB.OPTIMAL, GRB.SUBOPTIMAL):
    # Return the assignment of the jobs to the users.
    for i in steps:
        for j in users:
            if variables[i, j].X >= 1:
                assignment[i] = j
    return assignment
    # else:
    #     print("infeasible")


tasks = [1, 2, 3, 4, 5]
users = [1, 2, 3, 4, 5]

bod = [[1, 2]]
sod = [[3, 4]]

auths = [
    [1, 2],
    [1, 2],
    [3, 4],
    [3, 4],
    [5]
]

assignment = model_wsp(tasks, users, bod, sod, auths)
print(assignment)
