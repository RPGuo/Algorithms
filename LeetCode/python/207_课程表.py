class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        queue = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[course]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        return numCourses == 0