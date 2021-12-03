""" L1
Use hash table to save the first appeared characters of S and T.
"""
class Solution:
    def isIsomorphic(self, S: str, T: str) -> bool:
        D1, D2 = {}, {}
        for i, (s, t) in enumerate(zip(S, T)):
            if s not in D1: D1[s] = i
            if t not in D2: D2[t] = i
            if D1[s]!=D2[t]: return False
        return True