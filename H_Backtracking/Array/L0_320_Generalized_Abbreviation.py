""" https://leetcode.com/problems/generalized-abbreviation/
backtracking template with can_gen flag
"""

from header import *


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        stk = []

        def dfs(i, can_gen):
            if i == len(word):
                ans.append("".join(stk.copy()))
                return
            if can_gen:
                for j in range(i, len(word)):
                    stk.append(str(j - i + 1))
                    dfs(j + 1, False)
                    stk.pop()
            else:
                for j in range(i, len(word)):
                    stk.append(word[i : j + 1])
                    dfs(j + 1, True)
                    stk.pop()

        dfs(0, True)
        dfs(0, False)
        return ans
