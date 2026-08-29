class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight=max(weights)
        total=sum(weights)
        n=len(weights)
        res=max_weight*n
        left=max_weight
        right=max_weight*n

        while left<=right:
            mid=left+(right-left)//2

            days_needed = 1
            current_load = 0
            for w in weights:
                if current_load + w > mid:
                    days_needed += 1
                    current_load = 0
                current_load += w

            if days_needed<=days:
                res=min(res,mid)
                right=mid-1
            else:
                left=mid+1
        
        return res