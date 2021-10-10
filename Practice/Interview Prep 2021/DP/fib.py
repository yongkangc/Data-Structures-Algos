# bottom up

class Solution:
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.memo_fib(n)
    
    def memo_fib(self,n):
        cache = {0:0,1:1}
        
        for i in range(2,n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
            
        
# top down
class Solution:.

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.memo_fib(n)
    
    def memo_fib(self,n):
        cache = {0:0,1:1}
        
        if n in cache:
            return cache[n]
        
        cache[n] = self.memo_fib(n-1) + self.memo_fib(n-2)
        return cache[n]

class Solution:
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        self.cache = {0:0,1:1}
        
        return self.memo_fib(n)
    
    def memo_fib(self,n):
        if n in self.cache.keys():
            return self.cache[n]
        
        self.cache[n] = self.memo_fib(n-1) + self.memo_fib(n-2)
        
        return self.cache[n]