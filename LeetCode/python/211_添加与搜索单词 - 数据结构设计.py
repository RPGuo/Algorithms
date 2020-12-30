class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}
        self.end_of_word = '#'

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.tree
        for char in word:
            tree = tree.setdefault(char, {})
        tree['#'] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def dfs(word, tree):
            if not word:
                return '#' in tree
            if word[0] == '.':
                for t in tree:
                    if dfs(word[1:], tree[t]):
                        return True
            elif word[0] in tree:
                if dfs(word[1:], tree[word[0]]):
                    return True
            return False

        return dfs(word, self.tree)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)