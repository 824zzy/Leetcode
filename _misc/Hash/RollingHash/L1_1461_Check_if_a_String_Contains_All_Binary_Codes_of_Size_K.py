""" https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
Solution 1: rolling hash
1. hash function: hs = hs * size + val
2. update hash: hs -= val * size * (SeqSize-1)
Time complexity: O(n)

Solution 2: brute force to find all substring
Time complexity: O(n)
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

# brute force
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        A = []
        for i in range(len(s)):
            A.append(s[i])
            if i>=k-1: 
                seen.add(tuple(A))
                A.pop(0)
        return len(seen)==2**k