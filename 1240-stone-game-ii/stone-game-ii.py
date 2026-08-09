from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        s = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, m):
            if i == n:
                return 0

            ans = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                ans = max(ans, s[i] - dp(i + x, max(m, x)))
            return ans

        return dp(0, 1)