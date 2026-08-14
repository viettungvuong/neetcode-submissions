class Solution:
    def solve(self, board: List[List[str]]) -> None:
        moveX = [-1,0,0,1]
        moveY = [0,-1,1,0]

        rows = len(board)
        cols = len(board[0])

        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and (i,j) not in visited:
                    surrounded=True
                    q = [(i,j)]
                    to_capture=[]
                    while q:
                        currentX, currentY = q.pop(-1)

                        if currentX == 0 or currentX == rows-1 or currentY == 0 or currentY == cols-1:
                            surrounded=False

                        visited.add((currentX,currentY))
                        to_capture.append((currentX,currentY))

                        for k in range(4):
                            newX = currentX+moveX[k]
                            newY = currentY+moveY[k]

                            if newX >= 0 and newX < rows and newY >= 0 and newY < cols:
                                if board[newX][newY]=='O' and (newX,newY) not in visited:
                                    q.append((newX,newY))
                    
                    if surrounded==True:
                        while to_capture:
                            currentX, currentY = to_capture.pop()
                            board[currentX][currentY]='X'
