class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        hash_map = {}
        for s in strs:
            key = 1
            for char in s:
                key = key * prime[ord(char) - 97]
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return list(hash_map.values())
