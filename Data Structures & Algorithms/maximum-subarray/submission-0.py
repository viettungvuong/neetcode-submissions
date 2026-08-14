class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        n = len(nums)

        for i in range(1, n):
            current = max(nums[i], current + nums[i]) # add or not add
            best = max(current, best)
        
        return best