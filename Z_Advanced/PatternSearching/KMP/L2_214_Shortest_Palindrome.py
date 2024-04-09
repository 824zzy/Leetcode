""" https://leetcode.com/problems/shortest-palindrome/
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ss = s + "#" + s[::-1]
        lps = [0] * len(ss)  # longest prefix suffix array
        k = 0
        for i in range(1, len(ss)):
            while k and ss[k] != ss[i]:
                k = lps[k - 1]
            if ss[k] == ss[i]:
                k += 1
            lps[i] = k
        return s[k:][::-1] + s
