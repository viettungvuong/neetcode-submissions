class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moveX = [-1, 0, 0, 1]
        moveY = [0, -1, 1, 0]

        rows = len(grid)
        cols = len(grid[0])

        res = 0

        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    q = [(i,j)]
                    visited.add((i,j))
                    count = 0

                    while q:
                        x,y = q.pop(-1)

                        count+=1

                        for k in range(4):
                            newX = x+moveX[k]
                            newY = y+moveY[k]

                            if newX >= 0 and newX < rows and newY >= 0 and newY < cols:
                                if grid[newX][newY] == 1 and (newX,newY) not in visited:
                                    q.append((newX,newY))
                                    visited.add((newX,newY))
                    
                    res = max(res, count)
        
        return res
