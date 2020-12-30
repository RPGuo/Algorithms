# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(root, value):

            if not root:
                return
            value = value * 10 + root.val
            if not root.left and not root.right:
                self.res += value
                return
            if root.left:
                dfs(root.left, value)
            if root.right:
                dfs(root.right, value)

        dfs(root, 0)
        return self.res