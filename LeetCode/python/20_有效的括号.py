class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        param_dict = {')': '(', ']': '[', '}': '{'}
        for temp in s:
            if temp not in param_dict:
                stack.append(temp)
            elif not stack or stack.pop() != param_dict[temp]:
                    return False
        return not stack