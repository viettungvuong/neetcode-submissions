class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        moveX = [-1,0,0,1]
        moveY = [0,-1,1,0]

        for i in range(rows):
            for j in range(cols):
                if (i,j) in visited:
                    continue

                if grid[i][j] == '0':
                    continue

                # dfs
                st = [(i,j)]
                print(f"i: {i} - j: {j}")
                islands += 1

                while st:
                    currentX, currentY = st.pop()
                    visited.add((currentX, currentY))

                    for k in range(4):
                        newX = currentX + moveX[k]
                        newY = currentY + moveY[k]

                        if newX >= 0 and newX < rows and newY >= 0 and newY < cols:
                            if (newX, newY) not in visited and grid[newX][newY] == "1":
                                st.append((newX, newY))
        return islands

