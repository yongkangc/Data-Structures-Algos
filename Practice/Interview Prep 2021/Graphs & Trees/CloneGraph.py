# BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # BFS
    def cloneGraph(self, node: 'Node') -> 'Node':
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

# DFS iteratively
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
# DFS recursively
    def cloneGraph(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])