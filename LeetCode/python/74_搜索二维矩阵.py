class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                r -= 1
            elif matrix[mid // n][mid % n] < target:
                l += 1
        return False