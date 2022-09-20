""" https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
sliding window with hash table, the same as 159_Longest_Substring_with_At_Most_Two_Distinct_Characters_L0.py
"""
from header import *

class Solution:
    def lengthOfLongestSubstringKDistinct(self, A: str, k: int) -> int:
        seen = Counter()
        i = 0
        ans = 0
        
        for j in range(len(A)):
            seen[A[j]] += 1
            while len(seen)>k:
                seen[A[i]] -= 1
                if not seen[A[i]]: seen.pop(A[i])
                i += 1
            ans = max(ans, j-i+1)
        return ans