class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # pass 1: from left to right
        open_close = 0
        for i in range(n):
            if s[i] in "(*":
                open_close += 1
            else:
                open_close -= 1
            
            if open_close < 0:
                return False # not enough ( for )

        # pass 2: from right to left
        open_close = 0
        for i in range(n-1, -1, -1):
            if s[i] in ")*":
                open_close += 1
            else:
                open_close -= 1
        
            if open_close < 0:
                return False # not enough ) for (
        
        return True