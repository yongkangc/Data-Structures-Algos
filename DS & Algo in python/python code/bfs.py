import collections
# build a graph
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

# breath first search to traverse graph


def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            # adds all the vertices connected to vertex to the queue
            queue.extend(graph[vertex])

    return visited


def bfs2(self, node):  # BFS
    if not node:
        return None

    clone = {node: Node(val=node.val, neighbors=[])}
    queue = [node]
    while queue:
        print(queue)
        child = queue.pop(0)

        # visit neighbors
        for neighbor in child.neighbors:

            if neighbor not in clone:  # clone neighbor node and add that to the clone
                queue.append(neighbor)
                clone[neighbor] = Node(neighbor.val, [])

            clone[child].neighbors.append(clone[neighbor])

    return clone[node]


def dfs_iterative(self, node):
    if not node:
        return node
    root = Node(node.label)
    stack = [node]
    visit = {}
    visit[node.label] = root
    while stack:
        top = stack.pop()

        for n in top.neighbors:
            if n.label not in visit:
                stack.append(n)
                visit[n.label] = Node(n.label)
            visit[top.label].neighbors.append(visit[n.label])

    return root


data = pd.ExcelFile(
    "/work/inputs/Core Wallet Position _ PNL Manual Testing.xlsx")
wallet_4 = data.parse('4. 0x81...83bD (BEN_1) Txn')
wallet_6 = data.parse('6. 0xFA...f591 (SHIN ) Txn')
wallet_9 = data.parse('9. 0x47...0a7e (BEN_2) Txn')

wallet_array = [wallet_4, wallet_6, wallet_9]
for i in wallet_array:
    i.columns = i.iloc[0]
    i = i.drop(i.index[0])
    i["Average Cost Basis"] = np.nan

    i["Position"] = np.nan
    i["Profit"] = np.nan
    i["Returns"] = np.nan


# Convert row to column header
wallet_4.columns = wallet_4.iloc[0]
wallet_6.columns = wallet_6.iloc[0]
wallet_9.columns = wallet_9.iloc[0]

wallet_4 = wallet_4.drop(wallet_4.index[0])
wallet_6 = wallet_6.drop(wallet_6.index[0])
wallet_9 = wallet_9.drop(wallet_9.index[0])


wallet_4["Average Cost Basis"] = np.nan
wallet_4["Position"] = np.nan
wallet_4["Profit"] = np.nan
wallet_4["Returns"] = np.nan


wallet_6["Average Cost Basis"] = np.nan
wallet_6["Position"] = np.nan
wallet_6["Profit"] = np.nan
wallet_6["Returns"] = np.nan

wallet_9["Average Cost Basis"] = np.nan
wallet_9["Position"] = np.nan
wallet_9["Profit"] = np.nan
wallet_9["Returns"] = np.nan
