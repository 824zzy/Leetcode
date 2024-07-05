""" https://leetcode.com/problems/palindrome-rearrangement-queries/
the peak of categorization
"""
from header import *


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s) // 2
        t = s[n:][::-1]
        s = s[:n]
        pre1 = [Counter()]
        pre2 = [Counter()]
        pre3 = [0]
        cnt1 = Counter()
        cnt2 = Counter()
        diff = 0
        for i in range(n):
            cnt1[s[i]] += 1
            pre1.append(cnt1.copy())
            cnt2[t[i]] += 1
            pre2.append(cnt2.copy())
            if s[i] != t[i]:
                diff += 1
            pre3.append(diff)

        def check(a, b, c, d, pre1, pre2):
            # check if left and right range has different characters
            if pre3[a] > 0 or pre3[n] - pre3[max(b, d) + 1] > 0:
                return False
            # [a [c, d] b]
            if d <= b:
                # ensure S and T's characters in [a, b] are the same
                return (pre1[b + 1] - pre1[a]) == (pre2[b + 1] - pre2[a])
            # [a, b]...[c, d]
            if b < c:
                # ensure no different characters in [b, c]
                # ensure S and T's characters in [a, b] and [c, d] are the same
                return (
                    pre3[c] - pre3[b + 1] == 0
                    and pre1[b + 1] - pre1[a] == pre2[b + 1] - pre2[a]
                    and pre1[d + 1] - pre1[c] == pre2[d + 1] - pre2[c]
                )
            else:
                # [a,  b]
                #   [c,  d]
                # ensure S[a, b]-T[a, c] has same characters as T[c, d]-S[b, d]
                x, y = pre1[b + 1] - pre1[a], pre2[c] - pre2[a]
                xx, yy = pre2[d + 1] - pre2[c], pre1[d + 1] - pre1[b + 1]
                if x | y != x or xx | yy != xx:
                    return False
                s1 = x - y
                s2 = xx - yy
                return s1 == s2

        ans = [False] * len(queries)
        for i, (a, b, c, d) in enumerate(queries):
            c, d = 2 * n - 1 - d, 2 * n - 1 - c
            if a <= c:
                ans[i] = check(a, b, c, d, pre1, pre2)
            else:
                ans[i] = check(c, d, a, b, pre2, pre1)
        return ans


"""
"abcabc"
[[1,1,3,5],[0,2,5,5]]
"abbcdecbba"
[[0,2,7,9]]
"acbcab"
[[1,2,4,5]]
"deceecde"
[[3,3,6,7],[1,2,4,5],[2,3,7,7]]
"""
