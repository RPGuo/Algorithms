class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 10:
            return []
        hash_map = {}
        res = []
        for i in range(10, len(s)+1):
            tmp = s[i-10:i]
            if tmp in hash_map and hash_map[tmp] == 1:
                res.append(tmp)
            hash_map[tmp] = hash_map.get(tmp, 0) + 1
        return res