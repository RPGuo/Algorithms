class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(eval(b + i + a))))
            else:
                stack.append(i)
        return stack[-1]