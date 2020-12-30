# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.sol(pRoot)[0]
    def sol(self, root):
        if not root:
            return True, 0
        l_is, l_deep = self.sol(root.left)
        if not l_is:
            return False, -1
        r_is, r_deep = self.sol(root.right)
        if not r_is:
            return False, -1
        return abs(l_deep - r_deep) <= 1, max(l_deep, r_deep) + 1