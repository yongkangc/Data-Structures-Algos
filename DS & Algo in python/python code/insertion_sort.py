# 19/9/21
# Description: Bubble Sort
# Going to try it without referring to pseudocode


from random import randint
import random
from functools import wraps
from time import time
from random import randrange


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        # print('func:%r args:[%r, %r] took: %2.4f sec' %
        #       (f.__name__, args, kw, te-ts))
        print('func:%r took: %2.4f sec' %
              (f.__name__, te-ts))
        return result
    return wrap


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = i
        while arr[curr-1] > arr[curr] and curr > 0:
            arr[curr], arr[curr-1] = arr[curr-1], arr[curr]
            curr -= 1
    return arr


arr = [randint(0, 100) for p in range(0, 10)]
insertion_sort(arr) == sorted(arr)
print(insertion_sort(arr))


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        
        
        # populate the graph
        for edge in edges:
            node_1,node_2 = edge
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
        
        for node in self.graph:
            if node not in visited:
                self.dfs(node)
                count +=1
        
        return count

            
    def dfs(self,node):

        # mark it as visited
        self.visited.add(node)
        print(self.visited)


        # traverse the neighbors
        for neighbour in self.graph[node]:
            if neighbour not in self.visited:
                self.dfs(node,self.graph,self.visited)
                
            
    
