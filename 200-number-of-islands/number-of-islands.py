class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.helper(grid, i, j)
                    ans+=1
        return ans

    def helper(self, grid, i, j):
        if grid[i][j] != "1":
            return
        grid[i][j] = "2"
        if i-1 >= 0:
            self.helper(grid, i-1, j)
        if i+1 < len(grid):
            self.helper(grid, i+1, j)
        if j-1 >= 0:
            self.helper(grid, i, j-1)
        if j+1 < len(grid[0]):
            self.helper(grid, i, j+1)
        return