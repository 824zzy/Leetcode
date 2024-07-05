""" https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
think carefully about those cases!
"""


class Solution:
    def maximumTop(self, A: List[int], k: int) -> int:
        # if no moves allowed, just return the first element
        if k == 0:
            return A[0]
        # if only one element in the array, return by parity of k
        if len(A) == 1 and k > 0:
            if k & 1:
                return -1
            else:
                return A[0]

        a, b = -1, -1
        # case 1
        if A[: k - 1]:
            a = max(A[: k - 1])
        # case 2
        if k < len(A):
            b = A[k]
        return max(a, b)
