import Logic
import add
import ortool


def getFileInfo(filname):
    """
    Gets the raw data from a file and returns them as a list.
    Args:
        filname: The name of the file to be read.
    Returns:
        A list of lists containing the data from the file.
    """
    rawData = []
    with open(filname, 'r') as file:
        file = file.read()
        file = file.split("\n")
        for i in file:
            line = []
            splitline = i.split(",")
            for j in splitline:
                line.append(j.split())
            rawData.append(line)
    return rawData


def cleanData(data):
    """
    Removes empty lines from a list of lists.
    Args:
        data: A list of lists.
    Returns:
        A list of lists with empty lines removed.
    """
    cleaned = []
    for i in data:
        cleanline = []
        for j in i:
            if j:
                cleanline.append(j)
        if cleanline:
            cleaned.append(cleanline)
    return cleaned


def numPairsToList(str):
    """
    Takes a string of numbers and converts it to a list of tuples.
    Args:
        str: A string of numbers.
    Returns:
        output: A list of tuples.
    """
    str = str.replace("'", "")
    str = str.replace("[", "")
    str = str.replace("]", "")
    str = str.split(",")
    output = []
    for i in str:
        tup = i.split(":")
        tup[0] = int(tup[0])
        tup[1] = int(tup[1])
        output.append(tup)
    return output


def splitData(data):
    """
    Splits the data into the different constants.
    Args:
        data: A list of lists containing the data from the file.
    Returns:
        type: The type of the constraint.
        rules: A list of lists containing the rules both BOD and SOD.
        auths: A list of lists containing the auths.
    """
    type = str(data[0][0][0])
    numUsers = int(data[1][0][0])
    numSteps = int(data[2][0][0])
    bod = numPairsToList(str(data[3]))
    sod = numPairsToList(str(data[4]))
    authsString = str(data[5])
    authsString = authsString.replace("'", "")
    authsString = authsString.replace("[", "")
    authsString = authsString.replace("]", "")
    authsString = authsString.split(",")
    auths = []
    for i in authsString:
        tup = i.split(":")
        tupList = []
        for j in tup:
            tupList.append(int(j))
        auths.append(tupList)
    rules = []
    print(auths)
    for i in bod:
        rules.append([i[0], i[1], "BOD"])
    for i in sod:
        rules.append([i[0], i[1], "SOD"])
    return type, rules, auths


def computeSolution(solveType, rules, auths):
    """
    Takes the data and computes the solution. Picks the solver based on the solveType and calls the appropriate solver.
    Args:
        solveType: The type of solver to use.
        rules: A list of lists containing the rules both BOD and SOD.
        auths: A list of lists containing the auths.
    Returns:
        A list of lists containing the solution.
    """
    solution = []
    if solveType == "Brute":
        solution = Logic.main(rules, auths)
    elif solveType == "SAT":
        solution = ortool.SATsolver(rules, auths)
    elif solveType == "PBT":
        solution = add.pbtSolve(rules, auths)
    return solution


def writeOutput(solution):
    """
    Takes the solution and writes it to a file.
    Args:
        solution: A list of lists containing the solution.
    """
    with open("solution.txt", "w") as file:
        file.writelines(str(solution))


writeOutput(computeSolution(*splitData(cleanData(getFileInfo("file.csv")))))
