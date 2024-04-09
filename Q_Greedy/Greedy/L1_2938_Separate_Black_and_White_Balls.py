""" https://leetcode.com/problems/separate-black-and-white-balls/
linear scan to count how many '1' in the left side of '0'
"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            if s[i] == '0':
                ans += cnt
        return ans


"""
"101"
"100"
"0111"
"000"
"111"
"111000"
"01010001"
"""
