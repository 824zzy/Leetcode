""" https://leetcode.com/problems/largest-time-for-given-digits/
find and sort all possible time by permutation then find the maximal one
"""


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A = [[str(a) + str(b), str(c) + str(d)]
             for a, b, c, d in list(permutations(A))]
        A.sort(reverse=True)
        for x, y in A:
            if int(x) <= 23 and int(y) < 60:
                return ':'.join([str(x), str(y)])
        return ''
