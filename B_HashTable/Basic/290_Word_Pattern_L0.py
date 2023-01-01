""" https://leetcode.com/problems/word-pattern/
the same as 205
use two hash table to check pattern and s with each other
"""

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