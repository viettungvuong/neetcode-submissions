class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0

        n = len(nums)

        current_sum = 0
        res = 999999999999

        while l < n and r < n:
            current_sum += nums[r]

            while l <= r and current_sum >= target:
                print(f"{r} - {l}")
                res = min(res, r - l + 1)
                current_sum -= nums[l]
                l += 1
            
            r += 1
        if res == 999999999999:
            res = 0
        return res