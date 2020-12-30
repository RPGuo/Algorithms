# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if not queue or queue[0][1] > depth:
                res.append(node.val)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return res