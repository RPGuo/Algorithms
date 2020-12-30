# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.count = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        s = str(root.val) + ','
        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        return s+left+right
    def Deserialize(self, s):
        # write code here
        temp = s.split(',')
        self.count += 1
        node = None
        if temp[self.count] != '#':
            node = ListNode(int(temp[self.count]))
            node.left = self.Deserialize(s)
            node.right = self.Deserialize(s)
        return node