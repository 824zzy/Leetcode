""" https://leetcode.com/problems/letter-case-permutation/
use backtracking to iterateall
1. if s[i] is digit
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        stk = []
        ans = []

        def dfs(i):
            if i == len(s):
                return ans.append("".join(stk.copy()))
            if s[i].isdigit():
                stk.append(s[i])
                dfs(i + 1)
                stk.pop()
            else:
                for c in (s[i].lower(), s[i].upper()):
                    stk.append(c)
                    dfs(i + 1)
                    stk.pop()

        dfs(0)
        return ans
