# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if head.next == None:
            return TreeNode(head.val)

        slow, fast, pre = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        pre.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node