# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
### 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

### 非递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            next_stack = []
            for i in stack:
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
            stack = next_stack
            res += 1
        return res