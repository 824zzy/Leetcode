""" https://leetcode.com/problems/count-operations-to-obtain-zero/
keep substracting a or b until a==0 and b==0
"""


class Solution:
    def countOperations(self, a: int, b: int) -> int:
        ans = 0
        while a != 0 and b != 0:
            if a >= b:
                a -= b
            else:
                b -= a
            ans += 1
        return ans
