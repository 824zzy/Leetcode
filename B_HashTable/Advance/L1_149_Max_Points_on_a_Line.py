""" https://leetcode.com/problems/max-points-on-a-line/
Brute force to compute every slopes, and find the one has maximum frequency

Note that use gcd for higher precision is helpful even it is not necessary for this problem
"""


class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(len(A)):
            mp = defaultdict(int)
            x1, y1 = A[i]
            for j in range(len(A)):
                if i == j:
                    continue
                x2, y2 = A[j]
                if x1 == x2:
                    mp[(inf, inf)] += 1
                else:
                    dx, dy = x1 - x2, y1 - y2
                    # use gcd for higher precision
                    g = gcd(dx, dy)
                    dx, dy = dx // g, dy // g
                    mp[(dy, dx)] += 1
            ans = max(ans, 1 + max(mp.values(), default=0))
        return ans
