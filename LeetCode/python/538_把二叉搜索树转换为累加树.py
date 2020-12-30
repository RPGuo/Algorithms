# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack1, stack2, head = [], [], root
        while stack1 or root:
            if root:
                stack1.append(root)
                root = root.left
            else:
                root = stack1.pop()
                stack2.append(root)
                root = root.right

        for i in range(len(stack2) - 2, -1, -1):
            stack2[i].val += stack2[i + 1].val
        return head