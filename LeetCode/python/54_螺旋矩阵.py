class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        while True:
            for j in range(left, right + 1):
                res.append(matrix[up][j])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for j in range(right, left - 1, -1):
                res.append(matrix[down][j])
            down -= 1
            if up > down:
                break
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res