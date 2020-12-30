class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        res, visited = [], set()
        forward, backward = {beginWord: [[beginWord]]}, {endWord: [[endWord]]}
        _len = 2
        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
            temp = {}
            while forward:
                word, paths = forward.popitem()
                visited.add(word)
                for i in range(len(word)):
                    for a in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i] + a + word[i+1:]
                        if new in backward:
                            if paths[0][0] == beginWord:
                                res.extend(f_path + b_path[::-1] for f_path in paths for b_path in backward[new])
                            else:
                                res.extend(b_path + f_path[::-1] for f_path in paths for b_path in backward[new])
                        if new in wordList and new not in visited:
                            temp[new] = temp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):
                break
            forward = temp
        return res