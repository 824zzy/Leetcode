""" https://leetcode.com/problems/find-unique-binary-string/
Find unique binary string by backtracking
"""
from header import *

# bit mask solution


class Solution:
    def findDifferentBinaryString(self, A: List[str]) -> str:
        n = len(A)
        A = set(
            [sum(1 << i if b == "1" else 0 for i, b in enumerate(x[::-1])) for x in A]
        )
        self.mask = 0

        def dfs(i):
            if i == n:
                if self.mask not in A:
                    self.ans = bin(self.mask)[2:].rjust(n, "0")
                    return True
                else:
                    return False
            if dfs(i + 1):
                return True
            self.mask += 1 << i
            b = dfs(i + 1)
            self.mask -= 1 << i
            return b

        dfs(0)
        return self.ans


# stack solution


class Solution:
    def findDifferentBinaryString(self, A: List[str]) -> str:
        n = len(A)
        A = set(A)
        stk = []

        def dfs(i):
            if i == n:
                x = "".join(stk)
                if x not in A:
                    return x
                else:
                    return ""
            stk.append("0")
            a = dfs(i + 1)
            stk.pop()
            stk.append("1")
            b = dfs(i + 1)
            stk.pop()
            return a or b

        return dfs(0)
