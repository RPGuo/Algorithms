# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        def reverse(node):
            if not node or not node.next:
                return node
            head = reverse(node.next)
            node.next.next = node
            node.next = None
            return head

        def find_mid(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid_node = find_mid(head)
        head2 = mid_node.next
        mid_node.next = None
        head2 = reverse(head2)

        dummy = ListNode(-1)
        cur = dummy
        flag = True
        while head and head2:
            if flag:
                cur.next = head
                head = head.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
            flag = not flag
        cur.next = head if head else head2
        return dummy.next