""" https://leetcode.com/problems/single-row-keyboard/description/
hash table + simulation
"""

class Solution:
    def calculateTime(self, keyboard: str, A: str) -> int:
        mp = {k: i for i, k in enumerate(keyboard)}
        ans = mp[A[0]]
        for i in range(1, len(A)):
            ans += abs(mp[A[i]]-mp[A[i-1]])
        return ans