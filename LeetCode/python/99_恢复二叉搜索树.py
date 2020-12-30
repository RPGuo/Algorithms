# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node)
            helper(node.right)
        helper(root)
        node1 = None
        node2 = None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val:
                node2 = res[i+1]
                if node1 == None:
                    node1 = res[i]
        node1.val, node2.val = node2.val, node1.val