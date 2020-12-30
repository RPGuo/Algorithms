class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        rmL, rmR = 0, 0
        for char in s:
            if char == '(':
                rmL += 1
            elif char == ")":
                if rmL != 0:
                    rmL -= 1
                else:
                    rmR += 1
        def is_valid(s):
            count = 0
            for char in s:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                    if count < 0:
                        return False
            return True
        queue, visited = [], set()
        queue.append((s, rmL, rmR))
        visited.add((s, rmL, rmR))
        while queue:
            temp_s, temp_l, temp_r = queue.pop(0)
            if temp_l == 0 and temp_r == 0 and is_valid(temp_s):
                res.add(temp_s)
            for i in range(len(temp_s)):
                if temp_s[i] not in "()":
                    continue
                elif temp_s[i] == "(" and temp_l > 0:
                    t = (temp_s[:i]+temp_s[i+1:], temp_l-1, temp_r)
                    if t not in visited:
                        queue.append(t)
                        visited.add(t)
                elif temp_s[i] == ")" and temp_r > 0:
                    t = (temp_s[:i]+temp_s[i+1:], temp_l, temp_r-1)
                    if t not in visited:
                        queue.append(t)
                        visited.add(t)
        return list(res)