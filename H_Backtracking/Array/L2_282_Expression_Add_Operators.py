""" https://leetcode.com/problems/expression-add-operators/
"""


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def fn(i, expr, total, last):
            """Populate ans with expression evaluated to target."""
            if i == len(num):
                if total == target:
                    ans.append(expr)
            else:
                for ii in range(i, len(num) if num[i] != "0" else i + 1):
                    val = int(num[i:ii + 1])
                    if i == 0:
                        fn(ii + 1, num[i:ii + 1], val, val)
                    else:
                        fn(ii + 1,
                           expr + "*" + num[i:ii + 1],
                            total - last + last * val,
                            last * val)
                        fn(ii + 1, expr + "+" +
                           num[i:ii + 1], total + val, val)
                        fn(ii + 1, expr + "-" +
                           num[i:ii + 1], total - val, -val)

        ans = []
        fn(0, "", 0, 0)
        return ans


# brute force will TLE
class Solution:
    def addOperators(self, A: str, target: int) -> List[str]:
        stk = []
        ans = []

        def dfs(i, res, last):
            if stk and len(stk[-1]) > 1 and stk[-1][0] == '0':
                return
            if i == len(A):
                if res == target:
                    ans.append(''.join(stk.copy()))
                return True

            for j in range(i + 1, len(A) + 1):
                if not stk:
                    stk.append(A[i:j])
                    dfs(j)
                    stk.pop()
                else:
                    for op in ('+', '-', '*'):
                        stk.append(op)
                        stk.append(A[i:j])
                        f = dfs(j)
                        stk.pop()
                        stk.pop()

        dfs(0)
        return ans
