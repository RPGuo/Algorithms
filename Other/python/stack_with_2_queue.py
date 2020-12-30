class Solution():
    # 两个队列实现栈
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def pop(self):
        if self.queue1:
            return self.queue1.pop(0)
        elif self.queue2:
            return self.queue2.pop(0)
        else:
            return None

    def push(self, x):
        if not self.queue1:
            self.queue1.append(x)
        elif not self.queue2:
            self.queue2.append(x)
        if len(self.queue2) == 1 and len(self.queue1) >= 1:
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
        # len(self.queue2) 不可能为1，会被第一个if处理掉，到elif时要么是0要么是>=2
        elif len(self.queue1) == 1 and len(self.queue2) > 1:
            while self.queue2:
                self.queue1.append(self.queue2.pop(0))


if __name__ == '__main__':
    nums = [i for i in range(10)]
    test = Solution()
    for i in nums:
        test.push(i)
    res = [test.pop() for _ in range(len(nums))]
    print('stack_push: ' + str(nums))
    print('stack_pop: ' + str(res))