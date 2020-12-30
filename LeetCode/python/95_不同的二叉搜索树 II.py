# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        def helper(left, right):
            all_trees = []
            if left > right:
                return [None]
            for i in range(left, right + 1):
                left_tree = helper(left, i - 1)
                right_tree = helper(i + 1, right)
                for l in left_tree:
                    for r in right_tree:
                        cur_tree = ListNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_trees.append(cur_tree)
            return all_trees

        return helper(1, n)