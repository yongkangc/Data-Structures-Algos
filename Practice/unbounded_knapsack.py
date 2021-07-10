

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    # using recursive
    # base case

    if k <= 0 or len(arr) == 0:
        return 0

    elif arr[i] < loc :
        loc -= arr[i]
        loc = unboundedKnapsack(loc,arr)






if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = unboundedKnapsack(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()