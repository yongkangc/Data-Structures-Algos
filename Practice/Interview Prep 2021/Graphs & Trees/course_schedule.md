There are 2 ways to solve the problem

1. DFS :

- Marking the visited nodes as -1 for each node.
- if node v has not been visited, then mark it as 0.
- if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then it is a cycle.
- if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no cycle is being contained in v or its successors.

```python
# dfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for neighbor,node in prerequisites:
            graph[node].add(neighbor)
        self.visited_node = {i : 0 for i in range(numCourses)}
        for i in range(numCourses):
            if not self.dfs(i,graph):
                return False
        return True

    def dfs(self,node,graph):
        if self.visited_node[node] == -1:
            return False
        if self.visited_node[node] == 1:
            return True
        if self.visited_node[node] == 0:
            self.visited_node[node] = -1 # mark it as visited in the cycle
            for neighbor in graph[node]:

                if not self.dfs(neighbor,graph):
                    return False

        self.visited_node[node] = 1 # when the whole cycle is complete
        return True

```

2. BFS : Topological Sort

the idea is that if there is nothing point to that element, remove that element and its indegree to other elements. keep removing the indirection until there is no element left, or when the stack/queue is finished.

Have a outdegree to easily visit the neighbors

1. Identify a node with no incoming edges.
2. Add that node to the ordering.
3. Remove it from the graph.
4. Repeat.

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0 : return []

        outdeg = defaultdict(set)
        indeg = defaultdict(set)
        topo_sort = []

        # populate the graph
        for course in prerequisites:
            outdeg[course[1]].add(course[0])
            indeg[course[0]].add(course[1])

        # add the nodes where there is no items point to tehm in the queue
        queue = []

        for i in range(numCourses):
            if len(indeg[i]) == 0: # if nothing is pointing at it anymore
                queue.append(i) # we will be visiting these
                # remove all that is pointing to the node

        # bst
        while queue:
            node = queue.pop(0)

            topo_sort.append(node) # mark visited

            for neighbor in outdeg[node]: # from the node outdegree, remove the courses that has indegree pointing to them
                indeg[neighbor].remove(node)
                if len(indeg[neighbor]) == 0:
                    queue.append(neighbor)

            indeg.pop(node)


        return topo_sort if len(indeg.keys()) == 0 else []

# you would have to check if its true or false
# once you check if its true or false,
# we would have to do a bfs, and store the res
# this is essentially topological sort

# form graph and in degree
# if no more in degree, you put in q

```
