""" https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
brute force generate valid expressions and find the minimum
"""


class Solution:
    def minimizeResult(self, expression: str) -> str:
        A, B = expression.split("+")
        ans = eval(expression)
        res = "(" + expression + ")"
        for i in range(len(A)):
            for j in range(1, len(B) + 1):
                fl = int(A[:i]) if A[:i] else 1
                fr = int(B[j:]) if B[j:] else 1
                xl = int(A[i:])
                xr = int(B[:j])
                tmp = fl * (xl + xr) * fr
                if tmp < ans:
                    ans = tmp
                    res = A[:i] + "(" + str(xl) + "+" + str(xr) + ")" + B[j:]
        return res
