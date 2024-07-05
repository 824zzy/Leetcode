""" https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/submissions/
Use two pass monotonic stack to compute decreasing times and check if the minimal decreasing time is less than zero.

1. For the first pass from left to right, we use monotonic increasing stack to find next smallerer elements, if we find one, then pop the stack and increasing the dec1 by 1.
2. For the second pass from right to left, we use monotonic decreasing stack to find next larger elements, if we find one, then pop the stack and increasing the dec2 by 1.
3. Finally check if the minimal of dec1 and dec2 less or equal to 1.
Time complexity: O(n)
"""


class Solution:
    def canBeIncreasing(self, A: List[int]) -> bool:
        dec1 = 0
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]] >= A[i]:
                stk.pop()
                dec1 += 1
            stk.append(i)

        dec2 = 0
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]] <= A[i]:
                stk.pop()
                dec2 += 1
            stk.append(i)
        return min(dec1, dec2) <= 1


# brute force solution also works due to the low data size


class Solution:
    def canBeIncreasing(self, A: List[int]) -> bool:
        for i in range(len(A)):
            x = A[:i] + A[i + 1 :]
            if x == sorted(x) and len(x) == len(set(x)):
                return True
        return False
