""" https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
Translate the problem into how many beans are left after removal.
Since for A[i], there are A[i] * count(A[j]>=A[i]) beans left, the rest of the beans need to be removed.

1. sort the array
2. the beans will be removed can be represented as: sum(A)-A[i]*(len(A)-i)
"""


class Solution:
    def minimumRemoval(self, A: List[int]) -> int:
        A.sort()
        sm = sum(A)
        ans = []
        for i in range(len(A)):
            ans.append(sm - A[i] * (len(A) - i))
        return min(ans)
