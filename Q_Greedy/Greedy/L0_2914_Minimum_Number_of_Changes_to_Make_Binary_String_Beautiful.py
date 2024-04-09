""" https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
translate the problem into: make sure all the subarray of size 2 are either 00 or 11
"""


class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            if s[i:i + 2] != '00' and s[i:i + 2] != '11':
                ans += 1
        return ans


"""
"1001"
"10"
"0000"
"""
