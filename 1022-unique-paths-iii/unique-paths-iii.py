class Solution:
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])
        empty = 0
        sr = sc = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sr, sc = i, j
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(r, c, remain):
            if grid[r][c] == 2:
                return 1 if remain == 0 else 0

            temp = grid[r][c]
            grid[r][c] = -1

            paths = 0

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] != -1 and grid[nr][nc] != 1:
                        new_remain = remain - (1 if grid[nr][nc] == 0 else 0)
                        paths += dfs(nr, nc, new_remain)

            grid[r][c] = temp
            return paths

        return dfs(sr, sc, empty)