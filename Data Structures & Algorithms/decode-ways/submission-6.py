class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0]*n

        for i in range(n):
            if i==0:
                if s[i]=='0':
                    return 0
                else:
                    dp[i]=1
                    continue

            temp=s[i-1]+s[i]
            if s[i]=='0':
                if temp<"1" or temp>"26":
                    return 0
            else:
                dp[i]=dp[i-1]
            
            if temp>="1" and temp<="26":
                if i<2:
                    dp[i]+=1
                else:
                    dp[i]+=dp[i-2]
        
        return dp[n-1]


