# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        flag = False
        res = []
        stack = [root]
        while stack:
            temp_res = []
            temp_stack = []
            for node in stack:
                temp_res.append(node.val)
                if node.left:
                    temp_stack.append(node.left)
                if node.right:
                    temp_stack.append(node.right)
            stack = temp_stack
            if flag:
                temp_res = temp_res[::-1]
            res.append(temp_res)
            flag = not flag
        return res