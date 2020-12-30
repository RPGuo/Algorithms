# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
### 递归
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

### 非递归
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        level = 1
        while stack:
            next_stack = []
            for i in stack:
                if not i.left and not i.right:
                    return level
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
            stack = next_stack
            level += 1
        return level