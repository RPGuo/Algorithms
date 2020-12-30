class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mult = int(num1[i]) * int(num2[j])
                p1_index = i + j
                p2_index = i + j + 1
                num_sum = res[p2_index] + mult
                res[p1_index] += num_sum // 10
                res[p2_index] = num_sum % 10
        while res and res[0] == 0:
            res.pop(0)
        return ''.join(map(str, res)) if res else '0'