""" https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
observe the only two cases:
1. 010101...
2. 101010...
"""


class Solution:
    def minOperations(self, s: str) -> int:
        s = list(s)

        def fn(A, m):
            if m == 0:
                B = ['0' if i & 1 else '1' for i in range(len(A))]
            if m == 1:
                B = ['1' if i & 1 else '0' for i in range(len(A))]
            ans = 0
            for a, b in zip(A, B):
                if a != b:
                    ans += 1
            return ans

        return min(fn(s, 0), fn(s, 1))
