# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        res = self.is_sub_tree(pRoot1, pRoot2)
        if not res:
            res = self.is_sub_tree(pRoot1.left, pRoot2)
        if not res:
            res = self.is_sub_tree(pRoot1.right, pRoot2)
        return res
    def is_sub_tree(self, p1, p2):
        if not p2:
            return True
        elif not p1:
            return False
        elif p1.val != p2.val:
            return False
        else:
            return self.is_sub_tree(p1.left, p2.left) and self.is_sub_tree(p1.right, p2.right)