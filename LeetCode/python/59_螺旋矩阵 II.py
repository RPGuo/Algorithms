class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        up = left = 0
        down = right = n - 1
        count = 1
        while True:
            for j in range(left, right + 1):
                res[up][j] = count
                count += 1
            up += 1
            if count > n * n:
                break

            for i in range(up, down + 1):
                res[i][right] = count
                count += 1
            right -= 1
            if count > n * n:
                break

            for j in range(right, left - 1, -1):
                res[down][j] = count
                count += 1
            down -= 1
            if count > n * n:
                break

            for i in range(down, up - 1, -1):
                res[i][left] = count
                count += 1
            left += 1
            if count > n * n:
                break
        return res