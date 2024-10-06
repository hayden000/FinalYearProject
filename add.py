import ast

from unionfind import unionfind

import checkConstraints


def unify(bods, numsteps):
    """
    Runs the union find algorithm on the given list of bods.
    Args:
        bods list: the list of all bod constraints to be unified
        numsteps int:  the number of steps in the problem

    Returns:
    The groups of jobs that must be completed together
    """
    union = unionfind(numsteps)
    for i in bods:
        union.unite(i[0], i[1])
    union = union.groups()
    return union


def additem(lst, item):
    """
    Takes a list of lists and adds an item and produces all possible orderings with the new item included.
    Args:
        lst list: the list of lists to add the item to
        item int: the item to be added

    Returns:
    All possible orderings of the list with the new item included
    """
    output_list = []
    for i in range(len(lst)):
        temp = [j.copy() for j in lst]
        temp[i].append(item)
        output_list.append(temp)
    temp = [sublist.copy() for sublist in lst]
    temp.append([item])
    output_list.append(temp)
    return output_list


def pbtSolve(rules, auth):
    """
    The main function that runs the PBT algorithm.
    Args:
        rules list: the list of all constraints in the problem
        auth list: the list of all auth constraints in the problem
    Returns:
    The asssignments that satisfy all constraints with steps to users
    """
    step = len(auth)
    newrules = []
    for i in rules:
        newrules.append([int(i[0]) - 1, int(i[1]) - 1, i[2]])
    rules = newrules
    newauths = []
    for i in auth:
        sublist = []
        for j in i:
            sublist.append(j - 1)
        newauths.append(sublist)
    auth = newauths
    bod = []
    sod = []
    for i in rules:
        if i[2].upper() == "BOD":
            bod.append([i[0], i[1]])
        elif i[2].upper() == "SOD":
            sod.append([i[0], i[1]])

    class TreeNode:
        def __init__(self, value, children=None):
            """
            A tree structure to represent the possible orderings of the jobs.
            """
            self.value = value
            self.children = children if children is not None else []

    def eligibility_checker(auths, assignment):
        """
        Checks if a generated assignment of jobs is eligible based on the auth constraints.
        Args:
            auths list: the list of all auth constraints in the problem
            assignment list: the assignment of jobs to users to be checked

        Returns:
        True if the assignment is eligible, False otherwise
        """
        found = False
        if set(assignment).issubset(auths):
            found = True
        if not found:
            return False
        return True

    def checkPBT(lst, sod, bod):
        """
        Checks the non-unary constraints. If all constraints are satisfied, returns True.
        Args:
            lst list: the assignment of jobs to users to be checked
            sod list: the list of all sod constraints in the problem
            bod list: the list of all bod constraints in the problem

        Returns:
        true if all constraints are satisfied, false otherwise
        """
        allsod = True
        allbod = True
        for i in sod:
            if checkConstraints.checkSOD(i[0], i[1], lst) == False:
                allsod = False
        for i in bod:
            if checkConstraints.checkBOD(i[0], i[1], lst) == False:
                allbod = False
        if allbod and allsod:
            return True
        return False

    def generate_tree(node, sod, bod, depth):
        """
        A recursive function that generates all possible orderings of the jobs. And prunes the tree based on the constraints.
        Args:
            node TreeNode: the current node in the tree
            sod list: the list of all sod constraints in the problem
            bod list: the list of all bod constraints in the problem
            depth int: the depth of the tree

        Returns:
        The next level of the tree
        """
        if depth == -1:
            return node
        children = additem(node.value, depth)
        for child in children:
            child_node = TreeNode(child)
            node.children.append(child_node)
            generate_tree(child_node, sod, bod, depth - 1)
        return node

    root_value = []
    root = TreeNode(root_value)

    def print_tree(node, level=0):
        """
        A recursive function that prints the tree.
        Args:
            node TreeNode: the current node in the tree
        """
        print('  ' * level + str(node.value))
        for child in node.children:
            print_tree(child, level + 1)

    max_depth = step - 1
    tree = generate_tree(root, sod, bod, max_depth)

    def get_leaves(node):
        """
        Retrieves all the leaves of the tree.
        Args:
            node TreeNode: the current node in the tree

        Returns:
        The tree's leaves
        """
        if not node.children:
            return [node.value]
        else:
            leaves = []
            for child in node.children:
                leaves.extend(get_leaves(child))
        return leaves

    def compleateallocations(leaves, step):
        """
        Checks if a generated assignment of jobs contains all the jobs being allocated to users. If so it returns th matching.
        Args:
            leaves list: the tree's leaves
            step int: the number of steps in the problem

        Returns:
        Th matching
        """
        matching = []
        for leaf in leaves:
            if set(range(step)) == set([item for sublist in leaf for item in sublist]):
                matching.append(leaf)
        return matching

    import networkx
    def maxmatch(user, allocation, auth):
        """
        A function that implements the ford-fulkerson algorithm to find the maximum matching of the bipartite graph.
        Args:
            user int: the number of users in the problem
            allocation list: the assignment of jobs to find the matching for
            auth list: the list of all auth constraints in the problem

        Returns:
        A matching of the bipartite graph
        """
        Graph = networkx.Graph()
        users = []
        for i in allocation:
            Graph.add_node(str(i), Bipartite=1)
        for i in range(user + 1, len(auth) + user + 1):
            users.append(i)
        for i in users:
            Graph.add_node(i, Bipartite=0)
        for i in allocation:
            for j in auth:
                # print("j,i", (j, i))
                index_of_user = auth.index(j)
                if eligibility_checker(j, i):
                    Graph.add_edge(users[index_of_user], str(i))
        try:
            # pos = networkx.spring_layout(Graph)
            # networkx.draw(Graph, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10)
            # networkx.draw_networkx_edges(Graph, pos)
            # plt.title('Bipartite Graph')
            # plt.show()
            return networkx.bipartite.maximum_matching(Graph, top_nodes=users)
        except:
            return []

    leaves = get_leaves(tree)
    print_tree(tree)
    matches = compleateallocations(leaves, step)
    # Filtering to remove redudant matches
    valid = []
    for i in matches:
        if checkPBT(i, sod, bod):
            j = maxmatch(step, i, auth)
            if j != False:
                filtered_match = {}
                for key, value in j.items():
                    try:
                        int_key = int(key) - len(auth)
                        filtered_match[int_key] = value
                        steps = ast.literal_eval(value)
                        correct_steps = []
                        for i in steps:
                            i = i + 1
                            correct_steps.append(i)
                    except ValueError:
                        pass
                valid.append(filtered_match)

    print(valid)
    return valid


auth = [[1, 3, 4], [2], [3, 4], [3]]
rules = [[1, 2, "SOD"], [4, 3, "BOD"]]
pbtSolve(rules, auth)
