"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while cur:
            temp = cur.next
            copy_node = Node(cur.val, None, None)
            cur.next = copy_node
            copy_node.next = temp
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        copy_head = head.next
        cur = head
        copy_cur = copy_head
        while copy_cur.next:
            cur.next = cur.next.next
            cur = cur.next
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        cur.next = None
        copy_cur.next = None
        return copy_head