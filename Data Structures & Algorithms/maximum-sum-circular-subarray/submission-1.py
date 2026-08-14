class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best_max = nums[0]
        best_min = nums[0]
        total_sum = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        n = len(nums)

        for i in range(1, n):
            total_sum += nums[i]
            current_max = max(nums[i], current_max + nums[i])
            current_min = min(nums[i], current_min + nums[i])

            best_max = max(best_max, current_max)
            best_min = min(best_min, current_min)
        
        if best_max < 0:
            return best_max

        return max(best_max, total_sum - best_min)
