class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # come up with a memo according to the total amount +=1 -> amount
        dp = [0] + (amount+1) * [amount+1]

        # bottom up to calculate amount from 1 to amount.
        # for each amount, find the minimum number of coins needed and store that in
        for dp_amount in range(1, amount + 1):
            for coin in sorted(coins):

                if dp_amount < coin:  # break out of the loop as the amount is too low for coin
                    break

                # compare existing coins or memoised num of coin + current coin
                dp[dp_amount] = min(dp[dp_amount], dp[dp_amount - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
