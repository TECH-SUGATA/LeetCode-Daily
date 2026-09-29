class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2:
            return False

        # First must be '(' and last must be ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        from functools import lru_cache

        @lru_cache(None)
        def dfs(r, c, balance):
            # Add current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Invalid prefix
            if balance < 0:
                return False

            # Number of cells still left after current cell
            remaining = (m - 1 - r) + (n - 1 - c)

            # Even with all ')' we cannot reach 0
            if balance > remaining:
                return False

            # Destination
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Down
            if r + 1 < m and dfs(r + 1, c, balance):
                return True

            # Right
            if c + 1 < n and dfs(r, c + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)