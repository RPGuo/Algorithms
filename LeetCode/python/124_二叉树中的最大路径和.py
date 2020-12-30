# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res = max(self.res, left + right + node.val)
            ret = node.val + max(left, right)
            return ret if ret > 0 else 0
        helper(root)
        return self.res