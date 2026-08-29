class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = h*max(piles)
        piles = sorted(piles)
        res = max(piles)
        while left<=right:
            mid = left+(right-left)//2
            total = sum(math.ceil(p / mid) for p in piles)
            if total<=h:
                res=min(res,mid)
                right=mid-1
            else:
                left=mid+1
        
        return res