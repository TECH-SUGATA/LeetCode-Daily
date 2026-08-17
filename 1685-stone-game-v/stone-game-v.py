class Solution:
    def stoneGameV(self, a):
        n = len(a)
        p = [0]

        for x in a:
            p.append(p[-1] + x)

        memo = {}

        def dfs(l, r):
            if l == r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            ans = 0
            left = 0
            right = p[r + 1] - p[l]

            for k in range(l, r):
                left += a[k]
                right -= a[k]

                if left < right:
                    if ans < left * 2:
                        ans = max(ans, left + dfs(l, k))

                elif left > right:
                    if ans >= right * 2:
                        break
                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    ans = max(ans,
                              left + dfs(l, k),
                              right + dfs(k + 1, r))

            memo[(l, r)] = ans
            return ans

        return dfs(0, n - 1)