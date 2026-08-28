class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        intervals = sorted(intervals, key=lambda i: i[1])
        to_remove = 0
        prev_end = intervals[0][1]
        for i in range(1,n):
            if prev_end > intervals[i][0]:
                to_remove+=1
            else:
                prev_end=intervals[i][1]
        
        return to_remove