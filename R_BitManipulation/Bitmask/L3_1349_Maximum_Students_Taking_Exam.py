""" https://leetcode.com/problems/maximum-students-taking-exam/
1. Use bit mask to preprocess the seats
2. Row by row, check if the current mask if legit by five rules:
    x&A[i]==x: x is subset of A[i]
    (x>>1)&x==0: right seat is empty or broken
    (x<<1)&x==0: left seat is empty or broken
    (mask>>1)&x==0: top right seat is empty or broken
    (mask<<1)&x==0: top left seat is empty or broken
"""


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        A = []
        for row in seats:
            mask = 0
            for i, c in enumerate(row):
                if c == ".":
                    mask |= 1 << i
            A.append(mask)

        @cache
        def dp(i, mask):
            """
            x&A[i]==x: x is subset of A[i]
            (x>>1)&x==0: right seat is empty or broken
            (x<<1)&x==0: left seat is empty or broken
            (mask>>1)&x==0: top right seat is empty or broken
            (mask<<1)&x==0: top left seat is empty or broken
            """
            if i == len(A):
                return 0
            ans = dp(i + 1, 0)
            for x in range(1 << len(seats[0])):
                if (
                    x & A[i] == x
                    and (x << 1) & x == 0
                    and (x >> 1) & x == 0
                    and (mask >> 1) & x == 0
                    and (mask << 1) & x == 0
                ):
                    ans = max(ans, bin(x).count("1") + dp(i + 1, x))
            return ans

        return dp(0, 0)
