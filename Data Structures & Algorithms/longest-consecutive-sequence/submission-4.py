class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        print(nums)
        visited = set()
        for num in nums:
            visited.add(num)

        res = 1
        count = 1
        for num in nums:
            if num+1 in visited:
                count+=1
                res = max(res, count)
                print(f"{count} - {num} - {num+1}")
            else:
                count = 1
        return res