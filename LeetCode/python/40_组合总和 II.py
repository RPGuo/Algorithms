class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        n = len(candidates)
        candidates.sort()
        res = []

        def helper(i, temp, target):
            if target == 0:
                res.append(temp)
                return

            if i == n or target < candidates[i]:
                return

            for j in range(i, n):
                if (j > i and candidates[j] == candidates[j - 1]):
                    continue
                helper(j + 1, temp + [candidates[j]], target - candidates[j])

        helper(0, [], target)
        return res
