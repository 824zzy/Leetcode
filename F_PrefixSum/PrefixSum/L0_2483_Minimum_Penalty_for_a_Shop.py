""" https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
count the prefix and suffix of penalty and find the minimum one
"""


class Solution:
    def bestClosingTime(self, A: str) -> int:
        op = [0] * len(A)
        p = 0
        for i in range(len(A)):
            if A[i] == "N":
                p += 1
            op[i] = p
        op = [0] + op

        cl = [0] * len(A)
        p = 0
        for i in reversed(range(len(A))):
            if A[i] == "Y":
                p += 1
            cl[i] = p
        cl = cl + [0]
        return min([(o + c, i) for i, (o, c) in enumerate(zip(op, cl))])[1]
