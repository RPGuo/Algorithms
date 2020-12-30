class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(start, count, temp, target):
            if count == k:
                if target == 0:
                    res.append(temp)
                return
            for i in range(start, 10):
                if i > target:
                    break
                helper(i+1, count+1, temp+[i], target-i)
        helper(1, 0, [], n)
        return res