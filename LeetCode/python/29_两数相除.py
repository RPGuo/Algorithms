class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend > 0) ^ (divisor > 0)
        res = 0
        min_num = (-1 << 31)
        max_num = (1 << 31) - 1
        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = -divisor
        while (dividend <= divisor):
            temp_res = -1
            temp_div = divisor
            while (dividend <= (temp_div << 1)):
                if (temp_div <= min_num >> 1):
                    break
                temp_res = temp_res << 1
                temp_div = temp_div << 1
            dividend = dividend - temp_div
            res += temp_res

        if not flag:
            return max_num if res <= min_num else -res
        return res