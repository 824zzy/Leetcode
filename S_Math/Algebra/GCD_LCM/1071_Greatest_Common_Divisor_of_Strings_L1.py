""" https://leetcode.com/problems/greatest-common-divisor-of-strings/
find gcd of two string's length
"""
from header import *

class Solution:
    def gcdOfStrings(self, A: str, B: str) -> str:
        if A+B!=B+A: return ''
        g = gcd(len(A), len(B))
        return A[:g]

# or brute force
class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        for i in reversed(range(min(len(s1), len(s2)))):
            if len(s1)%(i+1)==0 and len(s2)%(i+1)==0:
                if s1[:i+1]*(len(s1)//(i+1))==s1 and s1[:i+1]*(len(s2)//(i+1))==s2:
                    return s1[:i+1]
        return ''