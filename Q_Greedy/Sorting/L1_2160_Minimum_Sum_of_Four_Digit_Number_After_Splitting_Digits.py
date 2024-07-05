""" https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
Intuition: We should always do a 2/2 split. 1/3 splits produce large sums.

So we greedily pick smallest digits and assign seperately to a and b.
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        A = sorted(map(int, list(str(num))))
        a, b = 0, 0
        for i in range(len(A)):
            if i & 1 == 0:
                a = 10 * a + A[i]
            else:
                b = 10 * b + A[i]
        return a + b


# suboptimal brute force


class Solution:
    def minimumSum(self, num: int) -> int:
        A = list(map(int, list(str(num))))
        ans = inf
        for a, b, c, d in list(permutations(A)):
            ans = min(ans, 10 * a + b + 10 * c + d)
        return ans
