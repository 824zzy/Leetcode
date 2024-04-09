""" https://leetcode.com/problems/append-k-integers-with-minimal-sum/
sort A then calculate the sum of (A[i]+1, min(A[i]+k, A[i+1]-1))
"""


class Solution:
    def minimalKSum(self, A: List[int], k: int) -> int:
        ans = 0
        A = sorted([0] + A + [inf])
        for i in range(len(A) - 1):
            if A[i] + 1 == A[i + 1]:
                continue
            l = A[i] + 1
            r = min(A[i] + k, A[i + 1] - 1)
            n = r - l + 1
            # (a_1+a_n)*n/2
            ans += (l + r) * (n) // 2
            k -= n
            if not k:
                break
        return ans
