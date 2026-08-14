class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        freq = {}
        pq = []

        prevNum = None

        for num in nums:
            if prevNum is not None and prevNum != num:
                heapq.heappush(pq, (-freq.get(prevNum), prevNum))
            if freq.get(num) is None:
                freq[num] = 0
            freq[num]+=1
            prevNum = num

        heapq.heappush(pq, (-freq.get(prevNum), prevNum))

        res = []
        for i in range(k):
            _, num = heapq.heappop(pq)
            res.append(num)

        return res

