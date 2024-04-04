""" https://leetcode.com/problems/word-pattern/
the same as 205
use two hash table to check pattern and s with each other
"""
from header import *

# on-the-fly solution
class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        if len(pattern)!=len(words.split()): return False
        p2w = {}
        w2p = {}
        for p, w in zip(pattern, words.split()):
            p2w.setdefault(p, w)
            w2p.setdefault(w, p)
            if p2w[p]!=w or w2p[w]!=p: return False
        return True
    
# 
class Solution:
    def isIsomorphic(self, S: str, T: str) -> bool:
        seenS, seenT = defaultdict(list), defaultdict(list)
        for i, (s, t) in enumerate(zip(S, T)):
            seenS[s].append(i)
            seenT[t].append(i)
        return sorted(seenS.values())==sorted(seenT.values())
            
"""
"abba"
"dog cat cat dog"
"abba"
"dog cat cat fish"
"aaaa"
"dog cat cat dog"
"abba"
"dog dog dog dog"
"aaa"
"aa aa aa aa"
"""