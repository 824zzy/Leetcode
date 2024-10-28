""" https://leetcode.com/problems/longest-palindromic-substring/
Manacher algorithm template
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#".join("^" + s + "$")
        half_len = [0] * (len(t) - 2)
        half_len[1] = 1
        box_m = box_r = max_i = 0
        for i in range(2, len(half_len)):
            hl = 1
            if i < box_r:
                hl = min(half_len[box_m * 2 - i], box_r - i)

            while t[i - hl] == t[i + hl]:
                hl += 1
                box_m, box_r = i, i + hl

            half_len[i] = hl
            if hl > half_len[max_i]:
                max_i = i
        hl = half_len[max_i]
        return s[(max_i - hl) // 2 : (max_i + hl) // 2 - 1]
