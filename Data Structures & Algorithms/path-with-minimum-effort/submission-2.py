class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        pq = []
        visited = set()
        cost = [[None for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    cost[i][j] = 0
                else:
                    cost[i][j] = 99999999
                heapq.heappush(pq, (cost[i][j], (i,j)))
        
        while pq:
            curr_cost, curr_pos = heapq.heappop(pq)
            x, y = curr_pos

            if curr_cost > cost[x][y]:
                continue
            if (x,y) in visited:
                continue

            cost[x][y] = curr_cost
            visited.add((x,y))

            moveX = [-1,0,0,1]
            moveY = [0,-1,1,0]

            for k in range(4):
                newX = moveX[k]+x
                newY = moveY[k]+y

                if newX>=0 and newY>=0 and newX<m and newY<n:
                    if (newX,newY) not in visited:
                        diff = abs(heights[x][y]-heights[newX][newY])
                        new_cost = max(curr_cost, diff) # cost is calculated by HIGHEST CONSECUTIVE diff
                        if new_cost < cost[newX][newY]:
                            cost[newX][newY] = new_cost
                            heapq.heappush(pq, (new_cost, (newX,newY)))
        return cost[m-1][n-1]