""" https://leetcode.com/problems/split-array-with-same-average/
https://leetcode.com/problems/split-array-with-same-average/discuss/120741/Python-Easy-and-Concise-Solution

Change the quesiton change to a N-sum problem:
To find if
1 element with sum = 1 * avg or
2 elements with sum = 2 * avg or
k elements with sum = k * avg

The size of smaller list between B and C will be less than N/2+1, so 0 < i < N/2+1

Recursive funciton find try to find a subset of n elements from A with sum = target
"""


class Solution:
    def splitArraySameAverage(self, A):
        @cache
        def find(target, k, i):
            if k == 0:
                return target == 0
            if target < 0 or k + i > n:
                return False
            return find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)

        n, s = len(A), sum(A)
        return any(
            find(s * k // n, k, 0) for k in range(1, n // 2 + 1) if s * k % n == 0
        )
