""" https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
trie + bit manipulation
1. build a bitwise trie based on 32 bits format numbers
2. greedily find numbers as opposite as possible from trie bit by bit
"""    
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
        for x in A: T.insert(bin(x)[2:].zfill(32))
            
        ans = 0
        for x in A:
            # find numbers as opposite as possible from trie bit by bit
            node = T.trie
            for c in map(int, bin(x)[2:].zfill(32)):
                # find opposite bit
                node = node.get(1-c) or node.get(c)
            ans = max(ans, x^node['#'])
        return ans