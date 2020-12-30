class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_num, min_num = (1<<31)-1, (-1<<31)
        is_first, flag, res = True, 1, 0
        for char in str:
            if char == ' ' and is_first:
                continue
            elif char == '-' and is_first:
                flag = -1
                is_first = False
            elif char == '+' and is_first:
                flag = 1
                is_first = False
            elif char >= '0' and char <= '9':
                is_first = False
                res = res*10 + int(char)
                if res*flag > max_num:
                    return max_num
                elif res*flag < min_num:
                    return min_num
            else:
                break
        return res*flag

### 正则表达式法
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = int(*re.findall(r'^[\+\-]?\d+', str.lstrip()))
        return max(min(temp, (1<<31)-1), (-1<<31))