# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        res = []
        for i in left + right:
            res.append([root.val] + i)

        return res