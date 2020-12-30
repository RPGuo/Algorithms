class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        hash_map = {}
        for task in tasks:
            hash_map[task] = hash_map.get(task, 0) + 1
        max_task = 0
        for i in hash_map:
            if hash_map[i] > max_task:
                max_task = hash_map[i]
        res = (max_task - 1) * (n + 1)
        for i in hash_map:
            if hash_map[i] == max_task:
                res += 1
        return res if res >= len(tasks) else len(tasks)