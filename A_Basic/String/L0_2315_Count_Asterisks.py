""" https://leetcode.com/problems/count-asterisks/
count * of even indexed segments
"""


class Solution:
    def countAsterisks(self, A: str) -> int:
        A = A.split("|")
        ans = 0
        for i in range(len(A)):
            if not i & 1:
                ans += A[i].count("*")
        return ans
