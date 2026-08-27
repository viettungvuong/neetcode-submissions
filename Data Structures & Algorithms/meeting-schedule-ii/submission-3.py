"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, tasks: List[Interval]) -> int:
        heap = []          # (end_time, machine_id)
        machines = {}      # machine_id -> [tasks]

        for t in sorted(tasks, key=lambda t: (t.start, t.end)):
            if heap and heap[0][0] <= t.start:      # inclusive: need strict 
                _, mid = heapq.heappop(heap)
            else:
                mid = len(machines)
                machines[mid] = []
            machines[mid].append(t)
            heapq.heappush(heap, (t.end, mid))

        return len(machines)