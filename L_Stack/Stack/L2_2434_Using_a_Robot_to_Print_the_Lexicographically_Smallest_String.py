""" https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
TODO: learn from: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/discuss/2678792/Python3-Stack-%2B-Counter-O(N)-Clean-and-Concise
"""
from header import *


class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        ans = []
        t = []

        for i, c in enumerate(s):
            t.append(c)
            cnt[c] -= 1
            if not cnt[c]:
                del cnt[c]
            while cnt and t and t[-1] <= min(cnt):
                ans += t.pop()
        ans += t[::-1]
        return "".join(ans)


""" "azz" "abc" "addb" "bdevfziy" "fnohopzv"
"zza"
"bac"
"bdda"
"bydizfve"
"vzhofnpo"
"""
