""" https://leetcode.com/problems/second-largest-digit-in-a-string/
find digits by set and sort them
"""
class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        for c in s:
            if c.isdigit():
                seen.add(int(c))
        if len(seen)<2: return -1
        else: return sorted(seen)[-2]