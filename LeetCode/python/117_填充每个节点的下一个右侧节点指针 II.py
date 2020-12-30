"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root or (not root.left and not root.right):
            return root
        if root.left and root.right:
            root.left.next = root.right
        node = root.right if root.right else root.left
        tail = root.next
        while tail and (not tail.left and not tail.right):
            tail = tail.next
        node.next = (tail.left if tail.left else tail.right) if tail else None

        self.connect(root.right)
        self.connect(root.left)
        return root