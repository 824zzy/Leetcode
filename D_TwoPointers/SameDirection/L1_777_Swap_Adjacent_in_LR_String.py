""" https://leetcode.com/problems/move-pieces-to-obtain-a-string/
777, 2337 are the same.

use two pointers to check if every pair of "L" and "R" is valid.
"""
class Solution:
    def canTransform(self, S: str, E: str) -> bool:
        n = len(S)
        i, j = 0, 0
        while i<n and j<n:
            while i<n and S[i]=='X': i += 1
            while j<n and E[j]=='X': j += 1
            if i==n or j==n: break
            elif S[i]!=E[j]: return False
            elif (S[i]=='L' and i<j) or (S[i]=='R' and i>j): return False
            i, j = i+1, j+1
        return 'L' not in S[i:] and 'R' not in S[i:] and 'L' not in E[j:] and 'R' not in E[j:]