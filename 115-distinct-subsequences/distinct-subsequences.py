class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp[j] = number of ways to form t[:j] from processed part of s
        dp = [0] * (n + 1)

        # Empty string can always be formed in 1 way
        dp[0] = 1

        for i in range(m):
            # Go backwards so previous values are not overwritten
            for j in range(n, 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]