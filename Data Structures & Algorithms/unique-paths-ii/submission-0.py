class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j]==1:
                    continue
                     
                if i==0 and j==0:
                    dp[i][j]=1
                    continue

                if i-1>=0 and obstacleGrid[i-1][j]==0:
                    dp[i][j]+=dp[i-1][j]
                if j-1>=0 and obstacleGrid[i][j-1]==0:
                    dp[i][j]+=dp[i][j-1]
        
        return dp[r-1][c-1]
                

                