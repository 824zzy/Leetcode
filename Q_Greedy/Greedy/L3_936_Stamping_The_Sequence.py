""" https://leetcode.com/problems/stamping-the-sequence/
greedily stamp the target sequence until the target becomes all "*" or cannot be stamped anymore.
"""


class Solution:
    def movesToStamp(self, s, t):
        n, m, t, s, ans = len(t), len(s), list(t), list(s), []
        f = True
        while t != ['*'] * n and f:
            for i in range(n - m + 1):
                # if any of i:i+m hasn't been stamped
                if t[i:i + m] != ['*'] * m:
                    f = True
                    # check if any invalid character to be stamped
                    for j in range(m):
                        if t[i + j] != '*' and not t[i + j] == s[j]:
                            f = False
                    # stamp if valid
                    if f:
                        t[i:i + m] = ['*'] * m
                        ans.append(i)

        if t == ['*'] * n:
            return ans[::-1]
        else:
            return []
