import networkx
from unionfind import unionfind

# Code to find a maximal matching of a bipartite graph
Graph = networkx.Graph()
users = ["A", "B", "C", "D", "E"]
step = 5
auth = [[0, 1, 2], [4], [5], [1], [0, 1, 2, 3, 4, 5]]
steps = []
BOD = [[0, 1], [1, 2]]
for i in range(0, step):
    steps.append(i)
union = unionfind(len(steps))
for i in BOD:
    union.unite(i[0], i[1])
union = union.groups()
for i in range(0, len(steps) + 1):
    if not any(i in sublist for sublist in union):
        union.append([i])
for i in union:
    Graph.add_node(str(i), bipartite=0)
for i in users:
    Graph.add_node(i, bipartite=1)
for i in range(0, len(users)):
    for j in union:
        if set(j).issubset(set(auth[i])):
            Graph.add_edge(str(j), users[i])
Graph.remove_nodes_from(list(networkx.isolates(Graph)))
pos = networkx.bipartite_layout(Graph, users)
# networkx.draw(Graph, pos, with_labels=True, node_color='lightblue')
# plt.title("Bipartite Graph Visualization")
# plt.show()

print(networkx.bipartite.maximum_matching(Graph))
