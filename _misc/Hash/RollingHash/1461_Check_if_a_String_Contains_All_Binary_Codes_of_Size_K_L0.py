""" https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
Solution 1: rolling hash
1. hash function: hs = hs * size + val
2. update hash: hs -= val * size * (SeqSize-1)

Solution 2: brute force
brute force find all substring
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        hs = 0
        for i in range(len(s)):
            hs = hs*2+int(s[i])
            if i>=k-1:
                seen.add(hs)
                hs -= int(s[i-(k-1)])*2**(k-1)
        return len(seen)==2**k
    
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        S = set()
        for i in range(len(s)-k+1): S.add(s[i:i+k])
        return len(S)==2**k