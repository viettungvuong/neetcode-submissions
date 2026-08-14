class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [100001]*(amount+1)
        for i in range(1,amount+1):
            if i in coins:
                dp[i]=1
            else:
                for j in range(1,i//2+1):
                    dp[i]=min(dp[j]+dp[i-j],dp[i])
        if dp[amount] == 100001:
            dp[amount] = -1
        return dp[amount]