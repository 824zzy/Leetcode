""" https://leetcode.com/problems/find-the-difference/
use two counters to find the only different element.
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t)-Counter(s)
        return [k for k, _ in diff.items()][0]

# or simply sum up the values and compute diffence, then convert it to a character
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))