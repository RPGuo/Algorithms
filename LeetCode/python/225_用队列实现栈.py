class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if not self.queue1:
            self.queue1.append(x)
        elif not self.queue2:
            self.queue2.append(x)

        if len(self.queue2) == 1 and len(self.queue1) >= 1:
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
        elif len(self.queue1) == 1 and len(self.queue2) > 1:
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue1:
            return self.queue1.pop(0)
        elif self.queue2:
            return self.queue2.pop(0)
        else:
            return False

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.queue1:
            return self.queue1[0]
        elif self.queue2:
            return self.queue2[0]
        else:
            return False

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1 and not self.queue2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()