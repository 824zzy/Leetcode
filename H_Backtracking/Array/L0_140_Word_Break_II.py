""" https://leetcode.com/problems/word-break-ii/
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        WD = set(wordDict)
        stk = []
        self.ans = []

        def dfs(i):
            if i >= len(s):
                return self.ans.append(" ".join(stk.copy()))

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in WD:
                    stk.append(s[i:j])
                    dfs(j)
                    stk.pop()

        dfs(0)
        return self.ans
