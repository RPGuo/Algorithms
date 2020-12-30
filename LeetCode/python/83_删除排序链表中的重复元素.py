# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head.next
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            else:
                fast = fast.next
        slow.next = None
        return head