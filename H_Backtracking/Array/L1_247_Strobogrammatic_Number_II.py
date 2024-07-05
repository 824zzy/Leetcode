""" https://leetcode.com/problems/strobogrammatic-number-ii/
be careful about the odd and even cases
"""
from header import *


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        mp = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }
        stk = []
        ans = []

        def dfs(i):
            if i == n // 2:
                if n & 1:
                    for c in "018":
                        s = str(int("".join(stk + [c] + [mp[x] for x in stk][::-1])))
                        if len(s) == n:
                            ans.append(s)
                else:
                    s = str(int("".join(stk + [mp[x] for x in stk][::-1])))
                    if len(s) == n:
                        ans.append(s)
                return

            for c in mp:
                stk.append(c)
                dfs(i + 1)
                stk.pop()

        dfs(0)
        return ans
