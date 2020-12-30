class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        clen = len(prerequisites)
        if clen == 0:
            return [i for i in range(numCourses)]

        in_degrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        for first, second in prerequisites:
            in_degrees[first] += 1
            adj[second].add(first)

        res = []
        queue = []
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(i)

        while queue:
            v = queue.pop(0)
            res.append(v)

            for w in adj[v]:
                in_degrees[w] -= 1
                if in_degrees[w] == 0:
                    queue.append(w)
        if len(res) != numCourses:
            return []
        return res