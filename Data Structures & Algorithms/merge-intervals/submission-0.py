class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i: i[0])
        n = len(intervals)

        prev_end = intervals[0][1]

        res = [intervals[0]]

        for i in range(1,n):
            if prev_end >= intervals[i][0]:
                res[-1][1]=max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
            prev_end = res[-1][1]

        return res