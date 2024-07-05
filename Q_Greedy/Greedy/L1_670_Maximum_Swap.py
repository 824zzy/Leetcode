""" https://leetcode.com/problems/maximum-swap/
greedy

1. use a suffix array to store the max index from i to the end
2. scan from left to right, if i!=suf[i] and A[i]!=A[suf[i]], swap them
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(str(num))
        suf = []
        mx_i = len(A) - 1
        for i in reversed(range(len(A))):
            if A[i] > A[mx_i]:
                mx_i = i
            suf.append(mx_i)
        suf.reverse()

        for i in range(len(A)):
            if i != suf[i] and A[i] != A[suf[i]]:
                A[i], A[suf[i]] = A[suf[i]], A[i]
                break
        return int("".join(A))


"""
2736
9973
98368
1993
"""
