""" https://leetcode.com/problems/different-ways-to-add-parentheses/
1. preprocessing the input string to separate numbers and operators
2. divide and conquer
"""

from header import *


class Solution:
    def diffWaysToCompute(self, E: str) -> List[int]:
        A = []
        i = 0
        while i < len(E):
            if i + 1 < len(E) and E[i].isdigit() and E[i + 1].isdigit():
                A.append(E[i] + E[i + 1])
                i += 2
            else:
                A.append(E[i])
                i += 1

        def dc(l, r):
            if l == r:
                return [int(A[l])]
            ans = []
            for i in range(l, r):
                if A[i].isdigit():
                    continue
                l_cands = dc(l, i - 1)
                r_cands = dc(i + 1, r)
                for lc in l_cands:
                    for rc in r_cands:
                        if A[i] == "+":
                            ans.append(lc + rc)
                        elif A[i] == "-":
                            ans.append(lc - rc)
                        elif A[i] == "*":
                            ans.append(lc * rc)
            return ans

        return dc(0, len(A) - 1)
