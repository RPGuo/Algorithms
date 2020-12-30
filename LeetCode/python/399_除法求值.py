class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (x, y), val in zip(equations, values):
            if x in graph:
                graph[x][y] = val
            else:
                graph[x] = {y: val}
            if y in graph:
                graph[y][x] = 1 / val
            else:
                graph[y] = {x: 1 / val}

        def _dfs(start, end):
            if start not in graph:
                return -1
            if start == end:
                return 1
            for node in graph[start].keys():
                if node == end:
                    return graph[start][node]
                if node not in visited:
                    visited.add(node)
                    v = _dfs(node, end)
                    if v != -1:
                        return graph[start][node] * v
            return -1

        res = []
        for (x, y) in queries:
            visited = set()
            res.append(_dfs(x, y))
        return res