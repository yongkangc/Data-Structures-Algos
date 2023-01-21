from typing import List

def maxProfit(prices: List[int]) -> int:
    loc_max, glo_max = 0, 0
    days_length = len(prices)
    for i in range(1,days_length):
        diff = prices[i] - prices[i-1]
        loc_max = max(0, loc_max + diff)
        glo_max = max(loc_max,glo_max)
    return glo_max

prices = [7,1,5,3,6,4]
print(maxProfit(prices))