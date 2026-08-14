class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)

        current_freq = 0

        prev = None
        print(nums)
        res = []

        for i in range(n):
            if prev is None or nums[i] == prev:
                current_freq += 1
            else:
                if current_freq > n / 3:
                    res.append(prev)
                current_freq = 1
            prev = nums[i]

        if current_freq > n / 3:
            res.append(prev)

        return res