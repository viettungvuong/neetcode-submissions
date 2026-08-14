class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0]*n

        res = 0

        for i in range(n):
            chosen = 0
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                chosen = max(chosen, dp[j])

            dp[i] = chosen + 1
            res = max(res, dp[i])
        
        return res
