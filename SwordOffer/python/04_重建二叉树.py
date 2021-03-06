# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        head = TreeNode(pre[0])
        index = tin.index(pre[0])
        head.left = self.reConstructBinaryTree(pre[1:index+1], tin[:index])
        head.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1:])
        return head