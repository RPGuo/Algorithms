# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node):
            if not node:
                return True, 0
            if not node.left and not node.right:
                return True, 1
            l_flag, l_depth = helper(node.left)
            if not l_flag:
                return False, -1
            r_flag, r_depth = helper(node.right)
            if not r_flag:
                return False, -1
            return abs(l_depth - r_depth) <= 1, max(l_depth, r_depth) + 1

        return helper(root)[0]