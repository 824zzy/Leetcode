""" https://leetcode.com/problems/sum-of-scores-of-built-strings/
https://cp-algorithms.com/string/z-function.html
Know it or lose it
"""


class Solution:
    def sumScores(self, s):
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z

        return sum(z_function(s)) + len(s)
