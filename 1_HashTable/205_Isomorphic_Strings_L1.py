""" https://leetcode.com/problems/isomorphic-strings/submissions/
Use hash table to save the first appeared characters of S and T.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mps, mpt = {}, {}
        for i, (ss, tt) in enumerate(zip(s, t)):
            if mps.get(ss)!=mpt.get(tt): return False
            mps[ss] = mpt[tt] = i
        return Trues