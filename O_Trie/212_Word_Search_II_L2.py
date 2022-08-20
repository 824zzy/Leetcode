""" https://leetcode.com/problems/word-search-ii/
trie + dfs

disgust time limit exceeded, to avoid this, we need a 
"""
class Trie:
    def __init__(self):
        self.trie = {}
    
    def insert(self, word):
        node = self.trie
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = word
        
class Solution:
    def findWords(self, A: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, node):
            if A[x][y] not in node: return
            if '#' in node[A[x][y]]:
                self.ans.append(node[A[x][y]]['#'])
                node[A[x][y]].pop('#') # pruning: avoid duplication
            
            for dx, dy in D: 
                if 0<=x+dx<len(A) and 0<=y+dy<len(A[0]):
                    tmp = A[x][y]
                    A[x][y] = '!'
                    dfs(x+dx, y+dy, node[tmp])
                    A[x][y] = tmp
            
        T = Trie()
        for w in words: T.insert(w)
        D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        self.ans = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                dfs(i, j, T.trie)
        return self.ans