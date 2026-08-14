class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        flow = [[""] * cols for _ in range(rows)]

        res = set()

        def dfs(x, y, to_mark):
            q = [(x,y)]
            while q:
                currentX, currentY = q.pop(-1)

                if to_mark in flow[currentX][currentY]:
                    continue

                flow[currentX][currentY] += to_mark

                if flow[currentX][currentY] == "AP" or flow[currentX][currentY] == "PA":
                    res.add((currentX,currentY))

                moveX = [-1,0,0,1]
                moveY = [0,-1,1,0]

                for i in range(4):
                    newX=currentX + moveX[i]
                    newY=currentY + moveY[i]
                    if newX>=0 and newX<rows and newY>=0 and newY<cols:
                        if heights[newX][newY]>=heights[currentX][currentY]:
                            if to_mark not in flow[newX][newY]:
                                q.append((newX,newY))

        # iterate cells on the outer (from ocean)
        # Pacific
        for col in range(cols):
            dfs(0,col,"P")

        for row in range(rows):
            dfs(row,0,"P")

        # Atlantic
        for col in range(cols):
            dfs(rows-1,col,"A")

        for row in range(rows):
            dfs(row,cols-1,"A")

        return list(res)

