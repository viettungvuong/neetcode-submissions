class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            heapq.heappush(pq, -num)

        res = None
        for i in range(k):
            res = heapq.heappop(pq)
        return -res