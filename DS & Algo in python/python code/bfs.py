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
            queue.extend(graph[vertex]) # adds all the vertices connected to vertex to the queue

    return visited

def bfs2(self, node): # BFS 
    if not node:
        return None
    
    clone = {node : Node(val=node.val,neighbors = [])}
    queue = [node]
    while queue:
        print(queue)
        child = queue.pop(0)
            
        # visit neighbors
        for neighbor in child.neighbors:
                        
            if neighbor not in clone: # clone neighbor node and add that to the clone
                queue.append(neighbor)
                clone[neighbor] = Node(neighbor.val,[])
                
            
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