""" https://leetcode.com/problems/minimum-window-subsequence/
top-down dp will TLE
"""
from header import *

# top-down dp will cause TLE


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        @cache
        def dp(i, j):
            if j == len(s2):
                return (i, 0)
            if i == len(s1):
                return (inf, inf)

            s, ans = dp(i + 1, j)
            if j != 0:
                ans += 1

            if s1[i] == s2[j]:
                ss, _ans = dp(i + 1, j + 1)
                _ans += 1
                if _ans <= ans and ss < s:
                    ans = _ans
                    s = ss
            return s, ans

        s, ans = dp(0, 0)
        if ans == inf:
            return ""
        return s1[s - ans : s]


# bottom-up dp which is the same as top-down dp
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        dp = [[inf for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(dp)):
            dp[i][-1] = i
        start = None
        l = inf
        for i in reversed(range(len(s1))):
            for j in reversed(range(len(s2))):
                s = dp[i + 1][j]
                if s1[i] == s2[j]:
                    ss = dp[i + 1][j + 1]
                    if ss < s:
                        s = ss
                dp[i][j] = s

            if dp[i][0] != inf and s - i <= l:
                start = i
                l = s - i

        if l == inf:
            return ""
        return s1[start : start + l]


# greedy + binary search to simulate
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        if len(s2) == 1:
            if s2[0] in s1:
                return s2
            else:
                return ""

        pos = defaultdict(list)
        for c2 in s2:
            if c2 in pos:
                continue
            for i, c1 in enumerate(s1):
                if c1 == c2:
                    pos[c1].append(i)
        path = [[x] for x in pos[s2[0]]]

        for i in range(1, len(s2)):
            nxt_path = []
            for p in path:
                idx = bisect_right(pos[s2[i]], p[-1])
                if idx >= len(pos[s2[i]]):
                    continue
                p.append(pos[s2[i]][idx])
                nxt_path.append(p)
            path = nxt_path
        if not path:
            return ""
        mn = min(path, key=lambda x: x[-1] - x[0])
        return s1[mn[0] : mn[-1] + 1]


"""
"abcdebdde"
"bde"
"jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
"u"
"abcdebde"
"bde"
"wcbsuiyzacfgrqsqsnodwmxzkz"
"xwqe"
"jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
"k"
"cnhczmccqouqadqtmjjzl"
"mm"
"""
