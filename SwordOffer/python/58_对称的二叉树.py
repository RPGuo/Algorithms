# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.is_same(pRoot.left, pRoot.right)
    def is_same(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.is_same(node1.left, node2.right) and self.is_same(node1.right, node2.left)
        return False