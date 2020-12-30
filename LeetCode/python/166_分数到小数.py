class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        a = numerator // denominator
        b = numerator % denominator
        res.append(str(a))
        if b == 0:
            return ''.join(res)
        res.append('.')
        dic = {b: len(res)}
        # -2.b
        while b:
            b = b * 10
            a = b // denominator
            b = b % denominator
            res.append(str(a))
            if b in dic:
                res.insert(dic[b], '(')
                res.append(')')
                break
            dic[b] = len(res)
        return ''.join(res)