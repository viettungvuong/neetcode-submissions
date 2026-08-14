class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        start = 0
        end = 0

        n = len(arr)

        while start < n:
            while end < n:
                if end-start+1 == 1 or (end-start+1 == 2 and arr[end] != arr[end-1]):
                    res=max(res,end-start+1)
                    end+=1
                    continue
                elif end-start+1 > 2 and (arr[end]-arr[end-1])*(arr[end-1]-arr[end-2])<0:
                    res=max(res,end-start+1)
                    end+=1
                    continue
                else:
                    break
            start+=1

        return res