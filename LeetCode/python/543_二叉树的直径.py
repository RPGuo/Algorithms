# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            self.res = max(self.res, l + r)
            return max(l, r) + 1
        helper(root)
        return self.res