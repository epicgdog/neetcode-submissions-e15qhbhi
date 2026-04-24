class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we want the find the number of islands
        # first find the first one
        # dfs to the neighbors that are ones
        # m = rows
        # n = cols
        # check if the i and j are within and n 
        # check if it is a 0 -> return
        # set that to 0
        # dfs(right), dfs(left), dfs(top), dfs(bottom)
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return;
            if grid[i][j] == '0':
                return;

            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # count the number of island
        # loop through grid, and then look for ones
        # dfs through that one
        total = 0;
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    total += 1
        return total

        