""" https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
brute force
"""


class Solution:
    def countPairs(self, A: List[int], k: int) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] == A[j] and (i * j) % k == 0:
                    ans += 1
        return ans
