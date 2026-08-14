class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0]*n

        wordDict = set(wordDict)

        validWordEnds = set()

        for i in range(n):
            if s[:i+1] in wordDict: # check substr from the start is a word
                dp[i]+=1
            if validWordEnds: # check substr continuing from a valid word substr
                for validWordEnd in validWordEnds:
                    if s[validWordEnd+1:i+1] in wordDict:
                        dp[i]+=dp[i-(i-validWordEnd)]
            
            if dp[i]>0:
                validWordEnds.add(i)

        return dp[n-1]>0
        