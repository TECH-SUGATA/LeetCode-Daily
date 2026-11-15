
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)

        # Store binary representations of powers of 5
        powers = set()
        x = 1

        while len(bin(x)[2:]) <= n:
            powers.add(bin(x)[2:])
            x *= 5

        # DP array
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue

            for j in range(i + 1, n + 1):
                if s[i:j] in powers:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != float('inf') else -1
