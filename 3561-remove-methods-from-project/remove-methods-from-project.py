from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]

        for u, v in invocations:
            g[u].append(v)

        s = set()

        def dfs(x):
            if x in s:
                return
            s.add(x)
            for y in g[x]:
                dfs(y)

        dfs(k)

        for u, v in invocations:
            if u not in s and v in s:
                return list(range(n))

        return [i for i in range(n) if i not in s]