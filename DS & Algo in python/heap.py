from collections import Counter

# building a heap allows us to perform it under n log n
# heap operations : extract min : o log n, insert : Ologn

# list -> counter -> heap
count = Counter(nums)
heapq.nlargest(k, count.keys(), key=count.get)