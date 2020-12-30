# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        res = []
        while stack1:
            temp = stack1.pop()
            stack2.append(temp)
            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)
        while stack2:
            res.append(stack2.pop().val)
        return res