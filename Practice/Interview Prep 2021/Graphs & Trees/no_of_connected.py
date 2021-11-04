# Using Union find

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            node = n1

            while node != par[node]:  # stop searching when the node is its own parent
                # path compressions
                # setting the parent of our node to the grandparent
                par[node] = par[par[node]]

                # if we dont find the root parent, update the current pointer as its own parent
                node = par[node]

            return node  # return the root parent

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0  # no union performed

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1  # return a successful union is performed

        # going through every single edge

        count = n
        for n1, n2 in edges:
            count -= union(n1, n2)

        return count
