class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res, path = [], []

        def dfs(start, temp_target):
            if temp_target == 0:
                res.append(path[:])
            for index in range(start, n):
                residue = temp_target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                dfs(index, residue)
                path.pop()

        dfs(0, target)
        return res