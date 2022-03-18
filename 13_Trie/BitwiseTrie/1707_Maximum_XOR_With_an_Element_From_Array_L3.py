""" https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
1. sort the array and queries to build bitwise trie on the fly
2. the remained problem is the same as 421
"""
class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        node = self.trie
        for c in map(int, word):
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = int(word, 2)
        
        
class Solution:
    def maximizeXor(self, A: List[int], queries: List[List[int]]) -> List[int]:
        A.sort()
        queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        T = Trie()
            
        ans = [-1] * len(queries)
        k = 0
        for m, x, idx in queries:
            while k<len(A) and A[k]<=m:
                T.insert(bin(A[k])[2:].zfill(32))
                k += 1
            node = T.trie
            if not node: continue
            for c in map(int, bin(x)[2:].zfill(32)):
                node = node.get(1-c) or node.get(c)
            ans[idx] = x^node['#']
        return ans
        