class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        is_primes = [1] * n
        is_primes[0] = is_primes[1] = 0
        ### 往后消除的话最小从 i^2 开始，因此 最外层循环 i^2 > n 的无需要考虑
        for i in range(2, int(n**0.5)+1):
            if is_primes[i]:
                j = i * i
                while j < n:
                    is_primes[j] = 0
                    j += i
        return sum(is_primes)