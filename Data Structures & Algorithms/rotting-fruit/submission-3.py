class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        q = []
        count_fresh = 0
        moveX=[-1,0,0,1]
        moveY=[0,-1,1,0]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    for k in range(4):
                        newX=i+moveX[k]
                        newY=j+moveY[k]
                        if newX>=0 and newX<rows and newY>=0 and newY<cols:
                            if grid[newX][newY]==1:
                                q.append((newX,newY))
                elif grid[i][j]==1:
                    count_fresh+=1

        res = 0
        visited = set()

        while q:
            for i in range(len(q)):
                currentX,currentY=q.pop(0)

                if (currentX,currentY) in visited:
                    continue

                if grid[currentX][currentY]==1:
                    grid[currentX][currentY]=2
                    count_fresh-=1

                if count_fresh<=0:
                    break

                visited.add((currentX,currentY))

                for k in range(4):
                    newX=currentX+moveX[k]
                    newY=currentY+moveY[k]
                    if newX>=0 and newX<rows and newY>=0 and newY<cols:
                        if grid[newX][newY]==1 and (newX,newY) not in visited:
                            q.append((newX,newY))

            res+=1

            if count_fresh <= 0:
                break

        if count_fresh > 0:
            return -1
        return res
                        