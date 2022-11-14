""" https://leetcode.com/problems/greatest-common-divisor-of-strings/
find gcd of two string's length
"""
class Solution:
    def gcdOfStrings(self, A: str, B: str) -> str:
        if A+B!=B+A: return ''
        g = gcd(len(A), len(B))
        return A[:g]

# or brute force
class Solution:
    def gcdOfStrings(self, A: str, B: str) -> str:
        cand = set()
        for i in reversed(range(len(A))):
            if len(A)%(i+1)==0:
                if A[:i+1] * (len(A)//(i+1))==A:
                    cand.add(A[:i+1])
                    
        
        for i in reversed(range(len(B))):
            if len(B)%(i+1)==0:
                if B[:i+1] * (len(B)//(i+1))==B and B[:i+1] in cand:
                    return B[:i+1]
        return ''