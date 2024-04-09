""" https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
count close parenthese at every dp state
"""


class Solution:
    def hasValidPath(self, A: List[List[str]]) -> bool:
        if A[0][0] == ')' and A[-1][-1] == '(':
            return False

        @cache
        def dp(i, j, cl):
            if not (0 <= i < len(A) and 0 <= j < len(A[0])):
                return False
            if i == len(A) - 1 and j == len(A[0]) - 1:
                return cl == 1

            ans = False
            if A[i][j] == '(':
                ans |= dp(i + 1, j, cl + 1)
                ans |= dp(i, j + 1, cl + 1)
            elif cl - 1 >= 0:
                ans |= dp(i + 1, j, cl - 1)
                ans |= dp(i, j + 1, cl - 1)
            return ans

        return dp(0, 0, 0)
