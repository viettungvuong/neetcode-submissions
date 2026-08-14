class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(n):
            # Odd case (center is s[i])
            tmp_str = expand(i, i)
            if len(tmp_str) > len(res): 
                res = tmp_str
            
            # Even case (center is between s[i] and s[i+1])
            tmp_str = expand(i, i + 1)
            if len(tmp_str) > len(res): 
                res = tmp_str
        return res
