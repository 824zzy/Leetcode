""" https://leetcode.com/problems/move-pieces-to-obtain-a-string/
777, 2337 are the same.

use two pointers to check if every pair of "L" and "R" is valid.

1. the order of letter in both s and t should be the same
2. from left to right, count the prefix sum of letter R
3. from right to left, count the prefix sum of letter L
"""


class Solution:
    def canChange(self, S: str, E: str) -> bool:
        n = len(S)
        i, j = 0, 0
        while i < n and j < n:
            while i < n and S[i] == "X":
                i += 1
            while j < n and E[j] == "X":
                j += 1
            if i == n or j == n:
                break
            elif S[i] != E[j]:
                return False
            elif (S[i] == "L" and i < j) or (S[i] == "R" and i > j):
                return False
            i, j = i + 1, j + 1
        return (
            "L" not in S[i:]
            and "R" not in S[i:]
            and "L" not in E[j:]
            and "R" not in E[j:]
        )


# prefix sum greedy solution
class Solution:
    def canChange(self, s: str, t: str) -> bool:
        ss, tt = "", ""
        for c1, c2 in zip(s, t):
            if c1 in ("L", "R"):
                ss += c1
            if c2 in ("L", "R"):
                tt += c2
        if ss != tt:
            return False

        cnt_s, cnt_t = 0, 0
        for c1, c2 in zip(s, t):
            if c1 == "R":
                cnt_s += 1
            if c2 == "R":
                cnt_t += 1
            if cnt_s < cnt_t:
                return False

        cnt_s, cnt_t = 0, 0
        for c1, c2 in zip(s, t):
            if c1 == "L":
                cnt_s += 1
            if c2 == "L":
                cnt_t += 1
            if cnt_s < cnt_t:
                return False
        return True
