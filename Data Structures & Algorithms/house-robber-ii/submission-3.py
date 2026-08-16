class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp_first = [0]*n
        dp_second = [0]*n

        for i in range(n):
            dp_first[i] = nums[i]
            dp_second[i] = nums[i]
        
        res=dp_first[0]

        # First pass: ignore the n-1 house
        for i in range(n-1):
            for j in range(i-1):
                dp_first[i]=max(dp_first[i], nums[i]+dp_first[j])
            res=max(dp_first[i],res)

        # Second pass: ignore the 0 house
        for i in range(1,n):
            for j in range(1,i-1):
                dp_second[i]=max(dp_second[i], nums[i]+dp_second[j])
            res=max(dp_second[i],res)

        return res

