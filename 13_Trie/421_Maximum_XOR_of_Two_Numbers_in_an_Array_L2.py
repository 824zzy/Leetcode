""" https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
trie + bit manipulation

build the trie on the fly and find numbers as opposite as possible from trie bit by bit
"""
# optimal solution: build trie on the fly
class Solution:
    def findMaximumXOR(self, A: List[int]) -> int:
        trie = {}
        ans = 0
        for x in A:
            n = bin(x)[2:].zfill(32)
            node = oppo = trie
            for c in map(int, n):
                node = node.setdefault(c, {})
                oppo = oppo.get(1-c) or oppo.get(c)
            node['#'] = x
            ans = max(ans, x^oppo['#'])
        return ans
    
# suboptimal solution
class Trie:
    def __init__(self):
        self.trie = defaultdict(dict)
        
    def insert(self, word: str) -> None:
        node = self.trie
        for c in map(int, word):
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = int(word, 2)
    
class Solution:
    def findMaximumXOR(self, A: List[int]) -> int:
        # insert binary representation of a number on a trie
        T = Trie()
        for x in A:
            n = bin(x)[2:].zfill(32)
            T.insert(n)
            
        ans = 0
        for x in A:
            # find numbers as opposite as possible from trie bit by bit
            node = T.trie
            for i in reversed(range(32)):
                # find opposite bit
                if x & (1<<i): val = 0 
                else: val = 1
                
                if val in node: node = node[val]
                elif 1-val in node: node = node[1-val]
                else: break
            ans = max(ans, x^node['#'])
        return ans