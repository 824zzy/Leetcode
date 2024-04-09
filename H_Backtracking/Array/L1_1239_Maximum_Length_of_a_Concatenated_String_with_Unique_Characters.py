""" https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
use backtracking to find out all possible combinations of strings
"""
from header import *


class Solution:
    def maxLength(self, A: List[str]) -> int:
        A = [x for x in A if len(x) == len(set(x))]
        stk = [0] * 26
        self.ans = 0

        def dfs(i):
            if i == len(A):
                self.ans = max(self.ans, sum(stk))
                return

            # skip to next string
            dfs(i + 1)
            a = []
            for c in A[i]:
                x = ord(c) - 97
                if not stk[x]:
                    a.append(x)
                else:
                    break
            else:
                # add current string
                for c in a:
                    stk[c] = 1
                dfs(i + 1)
                for c in a:
                    stk[c] = 0

        dfs(0)
        return self.ans


"""
["un","iq","ue"]
["cha","r","act","ers"]
["abcdefghijklmnopqrstuvwxyz"]
["aa","bb"]
"""
