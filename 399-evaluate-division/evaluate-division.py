class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        graph = defaultdict(dict)

        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return weight * result

            return -1.0

        answers = []

        for a, b in queries:
            answers.append(dfs(a, b, set()))

        return answers