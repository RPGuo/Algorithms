class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 0
        nums.sort()

        visited = [False] * len(nums)
        res = []

        def dfs(index, temp):
            if index == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]:
                    continue
                visited[i] = True
                temp.append(nums[i])
                dfs(index + 1, temp)
                visited[i] = False
                temp.pop()

        dfs(0, [])
        return res