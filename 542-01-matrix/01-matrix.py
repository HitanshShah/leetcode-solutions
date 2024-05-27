class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        max_val = rows*cols
        queue = deque()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = max_val
        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                r = row+dx
                c = col+dy
                if 0<=r<rows and 0<=c<cols and mat[r][c] > mat[row][col]+1:
                    queue.append((r,c))
                    mat[r][c] = mat[row][col]+1

        return mat