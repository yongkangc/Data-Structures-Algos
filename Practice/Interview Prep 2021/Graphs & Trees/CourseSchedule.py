# https://leetcode.com/problems/course-schedule/

# bfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 1 or 0:
            return True
        
        # create a graph with all the neighbors
        graph = defaultdict(set)
        indegree ={e : set() for e in range(numCourses) }
        
        for course in prerequisites:
            graph[course[1]].add(course[0]) #adding neighbour to node
            indegree[course[0]].add(course[1]) # adding what is pointing to that node
        
        # doing bfs to traverse and remove indirection
        queue = deque() # using deque as we want to pop left  
        for i,v in indegree.items():
            if len(v) == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            # remove course from the indegree and remove it from the set of its indegree from neighbors
            for neighbor in graph[course]:
                indegree[neighbor].remove(course)
                
            # adding nodes that no longer have anything pointing to them in the queue
                if len(indegree[neighbor]) == 0:
                    queue.append(neighbor)
                    
            indegree.pop(course)

            
        return not indegree
        


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
            self.visited_node[node] = -1
            for neighbor in graph[node]:
                
                if not self.dfs(neighbor,graph):
                    return False
        
        self.visited_node[node] = 1
        return True
        
        


        

        




 
        
        


        

        




