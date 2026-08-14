class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [100001]*(amount+1)
        dp[0] = 0

        # based on coin
        for coin in coins:
            if coin <= amount:
                for i in range(coin, amount+1):
                    dp[i] = min(dp[i], dp[i-coin]+1) # +1 for including the current coin
        if dp[amount] == 100001:
            dp[amount] = -1
        return dp[amount]