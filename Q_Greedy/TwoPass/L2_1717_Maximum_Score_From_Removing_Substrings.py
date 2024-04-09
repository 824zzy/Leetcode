""" https://leetcode.com/problems/maximum-score-from-removing-substrings/
Inspiration: If we split the string by characters other than "a" and "b". After serveral deletion, at the end there should be only "a"s or "b"s in the string.

1. swap (x, y) and reverse s if y>x
2. use two pass stack linear scans to first remove "ab" in s then remove "ba" in stk
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if y > x:
            x, y, s = y, x, s[::-1]
        ans = 0
        stk = []
        for c in s:
            stk.append(c)
            while len(stk) >= 2 and stk[-2:] == ['a', 'b']:
                stk.pop()
                stk.pop()
                ans += x

        stk2 = []
        for c in stk:
            stk2.append(c)
            while len(stk) >= 2 and stk2[-2:] == ['b', 'a']:
                stk2.pop()
                stk2.pop()
                ans += y
        return ans
