class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        n,m = len(grid), len(grid[0])
        res = 0

        def search(r,c):
            if (r<0 or c<0 or r>=n or c>=m or grid[r][c] == "0"):
                return 
            grid[r][c] = "0"
            for dr,dc in directions:
                search(r+dr,c+dc)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    search(i,j)
                    res += 1

        return res

