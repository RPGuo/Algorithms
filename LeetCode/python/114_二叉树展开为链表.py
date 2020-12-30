### 循环
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None
                root = root.right
        return root

### 递归
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        root.left = None
        root.right = l
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = r
        return root