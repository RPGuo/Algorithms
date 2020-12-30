# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [pRoot]
        res = []
        while stack:
            temp_stack = []
            temp_res = []
            for i in stack:
                temp_res.append(i.val)
                if i.left:
                    temp_stack.append(i.left)
                if i.right:
                    temp_stack.append(i.right)
            res.append(temp_res)
            stack = temp_stack
        return res