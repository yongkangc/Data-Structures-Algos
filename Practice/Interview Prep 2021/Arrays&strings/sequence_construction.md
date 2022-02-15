<https://leetcode.com/discuss/interview-question/1331495/amazon-oa-june-2021-winning-sequence>



```python
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'constructSequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER lo
#  3. INTEGER hi
#

def constructSequence(n, lo, hi):
    output = []
    total_num = hi - lo + 1
    if n > (total_num*2 -1) :
        output.append(-1)
        return output
    
    start = hi - 1
    if n > total_num + 1:
        start = hi - 1
    
    if n> total_num + 1:
        start = hi -(n - total_num)
    
    while start <= hi:
        output.append(start)
        start += 1
    
    start = hi - 1
    while start >= lo:
        output.append(start)
        if len(output) == n:
            return output
        start -= 1
    return output

# time : O(N)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    lo = int(input().strip())

    hi = int(input().strip())

    result = constructSequence(n, lo, hi)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```