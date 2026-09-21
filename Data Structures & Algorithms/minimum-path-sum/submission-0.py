class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                dp[i][j]=grid[i][j]
                if i-1>=0:
                    dp[i][j]+=dp[i-1][j]
                if j-1>=0:
                    if dp[i][j]==grid[i][j]:
                        dp[i][j]=grid[i][j]+dp[i][j-1]
                    else:
                        dp[i][j]=min(dp[i][j],grid[i][j]+dp[i][j-1])
        print(dp)
        return dp[r-1][c-1]

