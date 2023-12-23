""" https://leetcode.com/problems/number-of-divisible-substrings/
prefix sum simulation
"""
class Solution:
    def countDivisibleSubstrings(self, A: str) -> int:
        mp = {}
        for i in range(26):
            mp[chr(97 + i)] = (i + 4) // 3
        ans = 0
        for i in range(len(A)):
            sm = 0
            l = 0
            for j in range(i, len(A)):
                sm += mp[A[j]]
                l += 1
                if sm%l==0:
                    ans += 1
        return ans