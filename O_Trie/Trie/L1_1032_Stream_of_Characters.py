""" https://leetcode.com/problems/stream-of-characters/
note that execute "node = node[c]" first then "if '#' in node: return True"
"""


class StreamChecker:
    def __init__(self, words: List[str]):
        self.stk = []
        self.trie = {}
        for word in words:
            self.insert(word[::-1])

    def insert(self, word):
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = word

    def query(self, letter: str) -> bool:
        node = self.trie
        self.stk.append(letter)
        for c in reversed(self.stk):
            if c not in node:
                return False
            node = node[c]
            if '#' in node:
                return True
