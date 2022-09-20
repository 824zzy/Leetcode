""" https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
sliding window with hash table
"""
from header import *

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, A: str) -> int:
        seen = Counter()
        i = 0
        ans = 0
        
        for j in range(len(A)):
            seen[A[j]] += 1
            while len(seen)>2:
                seen[A[i]] -= 1
                if not seen[A[i]]: seen.pop(A[i])
                i += 1
            ans = max(ans, j-i+1)
        return ans
                
        
"""
"eceba"
"ccaabbb"
"""