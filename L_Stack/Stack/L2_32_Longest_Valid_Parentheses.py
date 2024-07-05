class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        start = 0
        stk = []
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            elif c == ")":
                if not stk:
                    start = i + 1
                else:
                    stk.pop()
                    if not stk:
                        ans = max(ans, i - start + 1)
                    else:
                        ans = max(ans, i - stk[-1])
        return ans
