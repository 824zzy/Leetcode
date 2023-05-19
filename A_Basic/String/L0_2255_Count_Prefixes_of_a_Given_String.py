""" https://leetcode.com/problems/count-prefixes-of-a-given-string/
basic usage of s.startswith
"""
class Solution:
    def countPrefixes(self, A: List[str], s: str) -> int:
        ans = 0
        for x in A:
            if s.startswith(x): ans += 1
        return ans