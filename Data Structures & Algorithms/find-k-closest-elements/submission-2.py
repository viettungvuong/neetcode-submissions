class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start_diff = None
        end_diff = None

        n = len(arr)

        for i in range(n-k+1):
            if start_diff and abs(x-arr[i+k-1]) >= start_diff and arr[i+k-1] != arr[i-1]:
                return arr[i-1:i+k-1]
            start_diff = abs(x-arr[i])
            end_diff = abs(x-arr[i+k-1])
            print(f"{start_diff} - {end_diff}")

        return arr[n-k:n]