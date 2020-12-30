# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next
            cur.next = pre
            pre = cur
        if fast:
            slow = slow.next
        while cur and slow:
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
        return True