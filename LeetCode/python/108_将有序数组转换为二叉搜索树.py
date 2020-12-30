# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        def helper(nums_list):
            if not nums_list:
                return None
            if len(nums_list) == 1:
                return TreeNode(nums_list[0])

            index = len(nums_list) // 2
            node = TreeNode(nums_list[index])
            node.left = helper(nums_list[:index])
            node.right = helper(nums_list[index + 1:])
            return node

        return helper(nums)