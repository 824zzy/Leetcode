""" Use two pointer in inside loop
sort string by length and lexicographical order 
and compare one by one.
"""
class Solution:
    def findLongestWord(self, s: str, D: List[str]) -> str:
        D = sorted(D, key=lambda x: (-len(x), x))
        for w in D:
            i = 0
            for j in range(len(s)):
                if w[i]==s[j]: i += 1
                if i==len(w): return w
        return ""