""" https://leetcode.com/problems/design-add-and-search-words-data-structure/
trie + dfs/bfs
"""
from header import *

# trie + dfs


class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, A: str) -> bool:
        def dfs(node, i):
            if i == len(A):
                return node.get('#', False)

            if A[i] == '.':
                return any([dfs(v, i + 1)
                           for k, v in node.items() if k != '#'])
            else:
                return A[i] in node and dfs(node[A[i]], i + 1)

        return dfs(self.trie, 0)

# trie + bfs


class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = {}

    def search(self, word: str) -> bool:
        Q = [self.trie]
        for c in word:
            nxtQ = []
            for node in Q:
                if c == '.':
                    for k, v in node.items():
                        nxtQ.append(v)
                elif c in node:
                    nxtQ.append(node[c])
            Q = nxtQ
        return any(['#' in node for node in Q])
