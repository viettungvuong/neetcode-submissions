class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land=2147483647
        moveX=[-1,0,0,1]
        moveY=[0,-1,1,0]

        rows=len(grid)
        cols=len(grid[0])

        chest_pos=set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0:
                    continue
                
                chest_pos.add((i,j))

        while chest_pos:
            current_chest = chest_pos.pop()
            x,y = current_chest
            for i in range(4):
                newX=x+moveX[i]
                newY=y+moveY[i]
                if newX<0 or newX>=rows or newY<0 or newY>=cols:
                    continue
                if grid[newX][newY]!=land and grid[newX][newY]<=0:
                    continue

                if grid[newX][newY]==land:
                    grid[newX][newY]=grid[x][y]+1
                    chest_pos.add((newX, newY))
                    print(f"Updated {newX}, {newY} from {x}, {y}")
                else:
                    if grid[newX][newY]>grid[x][y]+1:
                        grid[newX][newY]=grid[x][y]+1
                        chest_pos.add((newX, newY))
                        print(f"Updated {newX}, {newY} from {x}, {y}")

                