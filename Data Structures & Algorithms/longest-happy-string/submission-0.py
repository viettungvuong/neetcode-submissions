class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []

        if a>0:
            heapq.heappush(pq, (-a,"a"))
        if b>0:
            heapq.heappush(pq, (-b,"b"))
        if c>0:
            heapq.heappush(pq, (-c,"c"))

        res=""
        consecutive_count=0

        while pq:
            print(pq)
            current_count, current_char = heapq.heappop(pq)
            if len(res)>0 and current_char==res[-1]:
                consecutive_count+=1
            else:
                consecutive_count=1
            if consecutive_count==3:
                if pq:
                    prev_count, prev_char = current_count, current_char
                    current_count, current_char = heapq.heappop(pq)
                    consecutive_count=1
                    heapq.heappush(pq, (prev_count, prev_char))
                else:
                    break
            res+=current_char
            if abs(current_count)-1>0:
                heapq.heappush(pq, (current_count+1,current_char))
        
        return res