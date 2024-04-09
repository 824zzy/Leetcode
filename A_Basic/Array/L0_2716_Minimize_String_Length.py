""" https://leetcode.com/problems/minimize-string-length/
reading comprehension
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
