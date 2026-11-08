
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        cols = [0] * n

        # Count servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        # Count communicating servers
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1

        return ans
