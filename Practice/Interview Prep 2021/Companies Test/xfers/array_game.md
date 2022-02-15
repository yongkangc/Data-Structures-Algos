<https://leetcode.com/problems/minimum-moves-to-equal-array-elements/solution/>

```python
def countMoves(numbers):
    numbers.sort()
    moves = 0
    for i in range(1, len(numbers)):
        moves += numbers[i] - numbers[0] # using the current number to minus smallest
    return moves

# ON : O(NLOGN) due to sorting

if __name__ == '__main__':
```