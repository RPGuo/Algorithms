# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k <= 0:
            return None
        res = self.dfs(pRoot)
        return res[k-1] if len(res) >= k else None
    def dfs(self, pRoot):
        if not pRoot:
            return []
        left = self.dfs(pRoot.left)
        right = self.dfs(pRoot.right)
        return left+[pRoot]+right