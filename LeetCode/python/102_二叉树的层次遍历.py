# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
### BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            next_stack, temp_res = [], []
            for i in stack:
                temp_res.append(i.val)
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
            res.append(temp_res)
            stack = next_stack
        return res

### DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self._dfs(root, 0)
        return self.res

    def _dfs(self, root, level):
        if not root:
            return None
        if len(self.res) < level + 1:
            self.res.append([])
        self.res[level].append(root.val)
        self._dfs(root.left, level + 1)
        self._dfs(root.right, level + 1)