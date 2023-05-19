""" https://leetcode.com/problems/first-letter-to-appear-twice/
check if the character has been seen before.
"""
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cnt = Counter()
        for c in s:
            cnt[c] += 1
            if cnt[c]==2: return c