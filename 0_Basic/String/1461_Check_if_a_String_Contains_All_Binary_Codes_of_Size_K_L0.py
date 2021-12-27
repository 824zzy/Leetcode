""" https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
brute force find all substring
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        S = set()
        for i in range(len(s)-k+1): S.add(s[i:i+k])
        return len(S)==2**k