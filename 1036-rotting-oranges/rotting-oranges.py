class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # fresh = 0
        # ans = 0
        # queue = deque()
        # rows, cols = len(grid), len(grid[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             fresh+=1
        #         elif grid[i][j] == 2:
        #             queue.append([i, j])
        
        # directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # while queue and fresh>0:
        #     for i in range(len(queue)):
        #         r, c = queue.popleft()
        #         for dx, dy in directions:
        #             row, col = r+dx, c+dy
        #             if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
        #                 grid[row][col] = 2
        #                 queue.append([row, col])
        #                 fresh-=1
        #     ans+=1
        
        # if fresh>0:
        #     return -1
        # return ans

        fresh = 0
        ans = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while fresh > 0:
            curr = fresh
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        grid[i][j] = 3
                        for dx, dy in directions:
                            row, col = i+dx, j+dy
                            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                                grid[row][col] = 3
                                fresh-=1
            if curr == fresh:
                return -1
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
            ans += 1
            
        return ans