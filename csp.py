from ortools.sat.python import cp_model


def csp(at_least, at_most, equals, not_equals, auths):
    """
    A constraint satisfaction problem solver.
    Args:
        at_least: A list of lists of lists of integers. Each sublist is a list of lists of integers. The first integer is the number of jobs that must be completed. The second list is the list of jobs that must be completed.
        at_most: A list of lists of lists of integers. Each sublist is a list of lists of integers. The first integer is the number of jobs that must be completed. The second list is the list of jobs that must be completed.
        euals: A list of lists of integers. Each sublist is a list of integers. These represent the jobs that must be done together
        nnot_equals: A list of lists of integers. Each sublist is a list of integers. These represent the jobs that must not be done together
        auhts: A list of lists of integers. Each sublist is a list of integers. These represent the jobs that each user can do

    Returns:
    An asssignment of jobs to users.
    """

    def all_allocated(model, X):
        """
        Ensures that all jobs are allocated to a user.
        Args:
            mdoel: The model to be used
            X: The matrix of jobs
        """
        for i in range(0, len(X[0])):
            temp = []
            for j in range(0, len(X)):
                temp.append(X[j][i])
            model.Add(sum(temp) == 1)

    def add_at_least_constraint(model, X, S, l):
        """
        Adds the at least constraint to the model.
        Args:
            model: The model to be used
            X: The matrix of jobs
            S: The list of jobs that must be completed
            l: The number of jobs that must be completed

        """
        global temp
        for i in range(0, len(X)):
            temp = []
            for j in S:
                temp.append(X[i][j])
        model.Add(sum(temp) >= l)

    def add_at_most_constraint(model, X, S, u):
        """
        Adds the at most constraint to the model.
        Args:
            model: The model to be used
            X: The matrix of jobs
            S: The list of jobs that must be completed
            u: The upper bound number of jobs that can be completed

        """
        global temp
        for i in range(0, len(X)):
            temp = []
            for j in S:
                temp.append(X[i][j])
        model.Add(sum(temp) <= u)

    def equal(model, X, j1, j2):
        """
        Adds the equal constraint to the model.
        Args:
            mdoel: The model to be used
            X: The matrix of jobs
            j1: The first job
            j2: The second job
        """
        for i in range(0, len(X)):
            model.Add(X[i][j1] == X[i][j2])

    def non_equal(model, X, j1, j2):
        """
        Adds the not equal constraint to the model.
        Args:
            mdoel: The model to be used
            X: The matrix of jobs
            j1: The first job
            j2: The second job
        """
        for i in range(0, len(X)):
            model.Add(X[i][j1] + X[i][j2] <= 1)

    def shift_counting(lst):
        """
        Reduces the counting of jobs by one. To avoid indexing errors.
        Args:
            lst: The list to be reduced
        Returns:
            A list with the jobs reduced by one.
        """
        for i in lst:
            i[1] = [j - 1 for j in i[1]]
        return lst

    def recursive_shift(lst):
        """
        Reduces the counting of jobs by one. To avoid indexing errors. Using a recursive function.
        Args:
            lst: The list to be reduced
        Returns:
            A list with the jobs reduced by one.
        """
        if not lst:
            return lst
        if isinstance(lst[0], list):
            output = []
            for sublst in lst:
                output.append(recursive_shift(sublst))
            return output
        else:
            output = []
            for item in lst:
                output.append(item - 1)
            return output

    def add_auths(model, X, auth_list):
        """
        Implements the auths constraint.
        Args:
            mdoel: The model to be used
            X: The matrix of jobs
            auth_list: The list of jobs that each user can do
        """
        for i, auths in enumerate(auth_list):
            for j in range(0, len(X[0])):
                if j not in auths:
                    model.Add(X[i][j] == 0)

    model = cp_model.CpModel()
    at_least = shift_counting(at_least)
    at_most = shift_counting(at_most)
    equals = recursive_shift(equals)
    not_equals = recursive_shift(not_equals)
    auths = recursive_shift(auths)
    users = len(auths)
    unique = set()
    for i in auths:
        unique.update(i)
    steps = len(list(unique))
    X = []
    for i in range(1, users + 1):
        temp = []
        for j in range(1, steps + 1):
            var = model.NewBoolVar(str(i) + str(j))
            temp.append(var)
        X.append(temp)
    all_allocated(model, X)
    for i in at_most:
        add_at_most_constraint(model, X, i[1], i[0][0])
    for i in at_least:
        add_at_least_constraint(model, X, i[1], i[0][0])
    for i in equals:
        equal(model, X, i[0], i[1])
    for i in not_equals:
        non_equal(model, X, i[0], i[1])
    add_auths(model, X, auths)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    solution = []
    if status == cp_model.OPTIMAL:
        for i in range(0, users):
            for j in range(0, steps):
                if solver.Value(X[i][j]) == 1:
                    print(i + 1, "does", j + 1)
                    solution.append([i + 1, j + 1])
    return solution


def main():
    at_least = [[[2], [1, 2, 3, 4, 5, 6, 7]]]
    at_most = [[[2], [5, 6, 7]]]
    equals = [[2, 4]]
    not_equals = [[2, 3]]
    auths = [[1, 2, 3, 4, 6, 7], [2, 3, 4, 6], [4, 5, 6, 7]]
    csp(at_least, at_most, equals, not_equals, auths)


main()
