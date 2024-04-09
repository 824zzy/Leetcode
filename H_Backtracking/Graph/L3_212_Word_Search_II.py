""" https://leetcode.com/problems/word-search-ii/
trie + dfs + pruning

Pruning:
1. remove the matched word to avoid duplicates
2. incrementally remove the matched leaf node in Trie.

disgust time limit
"""
from header import *


class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word

        def search(p, x, y):
            node = p[A[x][y]]
            if '#' in node:
                ans.append(node['#'])
                # remove the matched word to avoid duplicates
                node.pop('#')
            tmp = A[x][y]
            A[x][y] = '!'
            for dx, dy in D:
                if 0 <= x + dx < len(A) and 0 <= y + \
                        dy < len(A[0]) and A[x + dx][y + dy] in node:
                    search(node, x + dx, y + dy)
            A[x][y] = tmp
            # Pruning: incrementally remove the matched leaf node in Trie.
            if not node:
                p.pop(A[x][y])

        D = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ans = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] in trie:
                    search(trie, i, j)
        return ans
