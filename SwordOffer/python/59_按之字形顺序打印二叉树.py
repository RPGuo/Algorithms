# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        res = []
        flag = False
        while stack:
            temp_stack = []
            temp_res = []
            for i in stack:
                temp_res.append(i.val)
                if i.left:
                    temp_stack.append(i.left)
                if i.right:
                    temp_stack.append(i.right)
            if flag:
                temp_res = temp_res[::-1]
            flag = not flag
            stack = temp_stack
            res.append(temp_res)
        return res