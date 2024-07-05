""" https://leetcode.com/problems/maximal-rectangle/
84 and 85 are similar problems.

85 = histogram model + monotonic stack(84)
"""


class Solution:
    def maximalRectangle(self, M: List[List[str]]) -> int:
        ans = 0
        A = [0] * len(M[0])
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == "1":
                    A[j] += 1
                else:
                    A[j] = 0
            # next smaller on the right
            R = [len(A)] * len(A)
            stk = []
            for i in range(len(A)):
                while stk and A[stk[-1]] > A[i]:
                    R[stk.pop()] = i
                stk.append(i)

            # next smaller on the left
            L = [-1] * len(A)
            stk = []
            for i in reversed(range(len(A))):
                while stk and A[stk[-1]] >= A[i]:
                    L[stk.pop()] = i
                stk.append(i)

            # for each A[i] as minimum, find the largest rectangle
            for i, (l, r) in enumerate(zip(L, R)):
                ans = max(ans, A[i] * (r - l - 1))
        return ans
