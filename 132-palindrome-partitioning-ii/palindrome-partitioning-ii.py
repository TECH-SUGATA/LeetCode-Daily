class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # dp[i][j] = True if s[i:j+1] is a palindrome
        palindrome = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        # cuts[i] = minimum cuts needed for s[0:i+1]
        cuts = [0] * n

        for i in range(n):
            cuts[i] = i

            for j in range(i + 1):
                if palindrome[j][i]:
                    if j == 0:
                        cuts[i] = 0
                    else:
                        cuts[i] = min(cuts[i], cuts[j - 1] + 1)

        return cuts[n - 1]