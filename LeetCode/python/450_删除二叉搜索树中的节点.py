# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == key:
            if not root.left: return root.right
            if not root.right: return root.left
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root