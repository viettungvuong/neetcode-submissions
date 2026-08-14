class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [1] * n
        min_dp = [1] * n

        for i in range(n):
            if i == 0:
                max_dp[i] = nums[i]
                min_dp[i] = nums[i]
                res = max_dp[i]
            else:
                choose_dp = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
                max_dp[i] = max(choose_dp, nums[i])

                choose_dp = min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i])
                min_dp[i] = min(choose_dp, nums[i])

                res = max(res, max_dp[i])
        
        return res
