""" https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
use set to count continous three characters are different or not
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                ans += 1
        return ans
