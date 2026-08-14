class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        res = 0

        for i in range(n):
            rob_from = 0
            for j in range(i-1):
                rob_from = max(rob_from, dp[j])

            dp[i] = rob_from + nums[i]
            res = max(res, dp[i])
        
        return res