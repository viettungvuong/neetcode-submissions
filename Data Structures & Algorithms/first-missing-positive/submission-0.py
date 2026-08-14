class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest_positive = 1

        visited = set()

        for num in nums:
            if num <= 0:
                continue

            visited.add(num)

        start = 1
        while True:
            if start not in visited:
                return start
            start += 1
        
        return 1