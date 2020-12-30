class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = n
        self.parent = [i for i in range(m)]
        self.rank = [0] * m

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        uf = UnionFind(M)
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count