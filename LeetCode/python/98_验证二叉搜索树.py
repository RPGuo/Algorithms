# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root, None, None)

    def helper(self, node, min_num, max_num):
        if not node:
            return True
        if min_num and min_num.val >= node.val:
            return False
        if max_num and max_num.val <= node.val:
            return False
        return self.helper(node.left, min_num, node) and self.helper(node.right, node, max_num)