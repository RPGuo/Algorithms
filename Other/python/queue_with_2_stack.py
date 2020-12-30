class Solution():
    # 两个栈实现队列
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, x):
        self.stack1.append(x)

    def delete_head(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()


if __name__ == '__main__':
    nums = [i for i in range(10)]
    test = Solution()
    for i in nums:
        test.append_tail(i)
    res = [test.delete_head() for _ in range(len(nums))]
    print('queue_append: ' + str(nums))
    print('queue_delete: ' + str(res))