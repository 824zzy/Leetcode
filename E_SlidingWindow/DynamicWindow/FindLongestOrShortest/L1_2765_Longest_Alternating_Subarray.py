""" https://leetcode.com/problems/longest-alternating-subarray/
track expected diff (+1/-1), restart smartly when pattern breaks on d==1
"""


class Solution:
    def alternatingSubarray(self, A: List[int]) -> int:
        ans = -1
        length = 1
        expect = 1
        for j in range(1, len(A)):
            d = A[j] - A[j - 1]
            if d == expect:
                length += 1
                expect = -expect
                ans = max(ans, length)
            elif d == 1:
                length = 2
                expect = -1
                ans = max(ans, length)
            else:
                length = 1
                expect = 1
        return ans
