# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        cur = head
        while cur:
            temp = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = temp
        return dummy.next

# tail指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        pre = dummy
        tail = dummy
        cur = head
        while cur:
            if tail.val < cur.val:
                tail.next = cur
                tail = cur
                cur = cur.next
            else:
                temp = cur.next
                tail.next = temp
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                cur.next = pre.next
                pre.next = cur
                pre = dummy
                cur = temp
        return dummy.next