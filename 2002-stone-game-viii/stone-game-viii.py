class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        ans = stones[n - 1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans