class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for c in s:
            if freq.get(c) is None:
                freq[c]=0
            freq[c]+=1

        pq = []
        for c, f in freq.items():
            heapq.heappush(pq, (-f, c))
        
        print(pq)

        n = len(s)
        res = ""
        last = None
        for i in range(n):
            temp = []
            selected = None
            selected_freq = 0
            while pq:
                selected_freq, selected = heapq.heappop(pq)
                if last is None or last != selected:
                    break
                else:
                    temp.append((selected_freq, selected))

            if selected == last:
                return ""

            res += selected
            last = selected
            if -selected_freq - 1 > 0:
                temp.append((selected_freq+1, selected)) 
            
            for t in temp:
                heapq.heappush(pq, t)
        
        return res
            


            