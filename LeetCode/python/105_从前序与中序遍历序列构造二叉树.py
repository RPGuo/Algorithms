# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:index+1], inorder[:index])
        node.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return node