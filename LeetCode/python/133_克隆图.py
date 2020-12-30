"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(node):

            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)
