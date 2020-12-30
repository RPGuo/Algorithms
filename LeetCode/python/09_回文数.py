### 分别取出来最左边和最右边的数字进行对比
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x // div >= 10:
            div *= 10
        while x:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x%div)//10
            div = div // 100
        return True

### 反转部分数字
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse_num = 0
        if x < 0 or (x!=0 and x%10==0):
            return False
        while x > reverse_num:
            reverse_num = reverse_num*10 + x%10
            x = x//10
        return x == reverse_num or x == reverse_num // 10