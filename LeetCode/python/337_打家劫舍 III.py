# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(node):
            if not node:
                return [0, 0]
            l = helper(node.left)
            r = helper(node.right)
            return [max(l)+max(r), node.val + l[0] + r[0]]
        return max(helper(root))