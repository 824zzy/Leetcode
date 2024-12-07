""" https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
greedy + two pointers
"""


class Solution:
    def canMakeSubsequence(self, s1: str, s2: str) -> bool:
        j = 0
        for i in range(len(s1)):
            if j < len(s2) and (
                s1[i] == s2[j]
                or chr(ord(s1[i]) + 1) == s2[j]
                or chr(ord(s1[i]) - 25) == s2[j]
            ):
                j += 1
        return j == len(s2)


"""
"abc"
"ad"
"zc"
"ad"
"ab"
"d"
"dm"
"e"
"""
