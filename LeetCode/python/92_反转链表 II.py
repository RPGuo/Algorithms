# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head:
            return None
        self.last_next = None

        def helper(node, k):
            if k == 1:
                self.last_next = node.next
                return node
            node_head = helper(node.next, k - 1)
            node.next.next = node
            node.next = self.last_next
            return node_head

        if m == 1:
            return helper(head, n)
        else:
            head.next = self.reverseBetween(head.next, m - 1, n - 1)
            return head