class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = sum(int(i)**2 for i in str(n))
        while slow != fast:
            slow = sum(int(i)**2 for i in str(slow))
            fast = sum(int(i)**2 for i in str(fast))
            fast = sum(int(i)**2 for i in str(fast))
        return slow == 1