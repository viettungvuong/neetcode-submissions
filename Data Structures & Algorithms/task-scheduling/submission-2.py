import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        q = []

        # 2. Initial heap: (-frequency, last_pos, task_name)
        # We use -1 for last_pos to indicate it hasn't been used yet
        for task, count in freq.items():
            heapq.heappush(q, (-count, -1, task))

        current_pos = 0
        res = []

        while q:
            chosen_task = None
            chosen_last_pos = None
            chosen_neg_freq = None
            not_met = []

            # 3. Look for the "most frequent" task that is NOT in cooldown
            while q:
                neg_freq, last_pos, task = heapq.heappop(q)

                if last_pos == -1 or current_pos - last_pos > n:
                    chosen_task = task
                    chosen_last_pos = last_pos
                    chosen_neg_freq = neg_freq
                    break
                
                # If it's in cooldown, save it to push back later
                not_met.append((neg_freq, last_pos, task))

            # Put the "not ready" tasks back into the heap
            for item in not_met:
                heapq.heappush(q, item)
            
            if chosen_task is not None:
                new_neg_freq = chosen_neg_freq + 1
                if new_neg_freq < 0:
                    heapq.heappush(q, (new_neg_freq, current_pos, chosen_task))
                res.append(chosen_task)
            else:
                res.append("Idle")
            
            current_pos += 1
            
        return current_pos