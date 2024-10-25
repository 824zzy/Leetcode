""" https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/
string simulation
"""

from header import *


class Solution:
    def stringSequence(self, t: str) -> List[str]:
        ans = ["a"]
        for i in range(len(t)):
            s = ans[-1]
            while s[-1] != t[i]:
                s = s[:-1] + chr(ord(s[-1]) + 1)
                ans.append(s)
            if i != len(t) - 1:
                ans.append(s + "a")
        return ans
