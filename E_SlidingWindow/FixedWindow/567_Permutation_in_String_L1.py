""" https://leetcode.com/problems/permutation-in-string/
the same as 438.

use a fixed sliding window and a Counter to record p's frequency
when Counter values are all 0, an answer is found.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        for i in range(len(s2)):
            cnt[s2[i]] -= 1
            if i>=len(s1): cnt[s2[i-len(s1)]] += 1
            if all(x==0 for x in cnt.values()): return True
        return False


# Or Brute force
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)])==cnt1: return True
        return False