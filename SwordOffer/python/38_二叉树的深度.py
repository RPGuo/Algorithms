# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        stack = [pRoot]
        count = 0
        while stack:
            new_stack = []
            for i in stack:
                if i.left:
                    new_stack.append(i.left)
                if i.right:
                    new_stack.append(i.right)
            stack = new_stack
            count += 1
        return count