# Best Time to buy and sell stocks

There are multiple ways to do these

1. Kadane's Algorithm
2. Sliding window/Two pointer

- Left pointer is the buy day
- Right pointer is the sell day
- Keep track of the max profit
- Move the right pointer always
- The left pointer should be the min. therefore if left > right, move left to right

## Kadane's Algorithm

```python
    def maxProfit(self, prices: List[int]) -> int:
        loc_max, glo_max = 0, 0
        days_length = len(prices)
        for i in range(1,days_length):
            diff = prices[i] - prices[i-1]
            loc_max = max(0, loc_max + diff)
            glo_max = max(loc_max,glo_max)
        return glo_max
```
- Local max is the max profit we can get if we sell on the current day
- For each day, we calculate the difference between the current day and the previous day
- If the difference is positive, we add it to the local max.
- If the difference is negative, we reset the local max to 0.
- We find the max of diff + local max because as long as the total local max is positive, we can sell on the current day. 
