from csp import csp

for l in range(0, 10):
    """
    Loop for generating instances
    """
    print("instance", l)
    import math
    import random


    def outputAssignment(assignment):
        """
        A function for outputting the assignment
        Args:
            assignment: the assignment
        """
        for i in range(1, len(assignment)):
            random.shuffle(assignment[i])
            print("user ", i, " does ", assignment[i])


    def computeMinSublistLength(lst):
        """
        A function for computing the minimum length of a sublist
        Args:
            lst: the list
        Returns:
            The minimum length of a sublist
        """
        length = math.inf
        for i in lst:
            length = min(length, len(i))
        return length


    def createModel(steps, users):
        """
        Build a model
        Args:
            steps: the number of steps
            users: the number of users
        Returns:
            A random model
        """
        solution = []
        for i in range(1, users + 1):
            solution.append([])
        for i in range(1, steps + 1):
            solution[random.randrange(1, users)].append(i)
        return solution


    def atLeastmin(solution):
        """
        A function for computing the at least constraint
        Uses the min sublist to compute the at least constraint
        Args:
            solution: the solution
        Returns:
            The at least constraint
        """
        atLeast = []
        minamount = computeMinSublistLength(solution)
        for i in solution:
            for j in i[1:minamount]:
                atLeast.append(j)
                random.shuffle(atLeast)
        outputAtLeast = [[minamount], atLeast]
        return [outputAtLeast]


    def atMost(solution):
        """
        A function for computing the at most constraint
        Uses largest sublist to compute the at most constraint
        Args:
            solution: the solution
        Returns:
            The at most constraint
        """
        best = 0
        for i in range(0, len(solution)):
            if (len(solution[i]) > best):
                best = i
        random.shuffle(solution[best])
        outputatmost = [[len(solution[best])], solution[best]]
        return [outputatmost]


    def equal(solution):
        """
        Computes groups of jobs that must be done by the same user
        Args:
            solution: the solution
        Returns:
            The bod constraints
        """
        pairs = []
        for sub_lst in solution:
            for i in range(0, len(sub_lst) - 1):
                pairs.append([sub_lst[i], sub_lst[i + 1]])
        return pairs


    def pair_first_items(solution):
        """
        Finds eaual constraints by finding the first item of each sublist and paired with the next sublist's first item
        Args:
            solution: the solution
        Returns:
            paired items for SOD constraints
        """
        pairs = []
        for i in range(0, len(solution) - 1):
            try:
                pairs.append([solution[i][0], solution[i + 1][0]])
            except:
                continue
        return pairs


    def computeAuths(solution, steps):
        """
        Augments the authauthorsation constraint
        Args:
            solution: the solution
        Returns:
            The new authauthorsation constraint
        """
        output = []
        for i in solution:
            temp = []
            for j in i:
                temp.append(j)
            for j in range(1, random.randrange(1, steps)):
                addstep = random.randrange(1, steps)
                if addstep not in temp:
                    temp.append(addstep)
            output.append(temp)
        return output


    # Calling the functions
    steps = random.randrange(45, 70)
    users = random.randrange(5, 15)
    solution = createModel(steps, users)
    authsoutput = computeAuths(solution, steps)
    outputatmost = atMost(solution)
    outputAtLeast = atLeastmin(solution)
    outputEqual = equal(solution)
    notequal = pair_first_items(solution)
    random.shuffle(outputEqual)
    random.shuffle(notequal)
    print("at most:", outputatmost)
    print("at least:", outputAtLeast)
    print("equal:", outputEqual)
    print("not equal:", notequal)
    print("auths:", authsoutput)
    # Calling the CSP solver
    print("CSP solution", csp(outputAtLeast, outputatmost, outputEqual, notequal, authsoutput))
    outputAssignment(solution)
