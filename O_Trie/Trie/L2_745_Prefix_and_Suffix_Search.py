""" https://leetcode.com/problems/prefix-and-suffix-search/
Learn from hint: For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test". Then if we have a query like prefix = "te", suffix = "t", we can find it by searching for something we've inserted starting with "t#te".
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, i, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node["#"] = i
            node = node[c]
        node["#"] = i

    def search(self, word):
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return -1
        return node["#"]


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words):
            for k in range(len(word)):
                key = word[k:] + "$" + word
                self.trie.insert(i, key)

    def f(self, prefix: str, suffix: str) -> int:
        key = suffix + "$" + prefix
        return self.trie.search(key)
