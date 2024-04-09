""" https://leetcode.com/problems/steps-to-make-array-non-decreasing/
This is actually a pretty hard problem. The solution is from lee: https://leetcode.com/problems/steps-to-make-array-non-decreasing/discuss/2085864/JavaC%2B%2BPython-Stack-%2B-DP-%2B-Explanation

1. apply monotonic decreasing stack to the reversed array to find the next greater element.
2. while find a greater element, here is the magic: pop every smaller element in the stack and
    1. dp[i] means the number of element A[i] can eat.
    2. `max(dp[stk.pop()], dp[i]+1)` to update dp[i]
"""


class Solution:
    def totalSteps(self, A: List[int]) -> int:
        A.reverse()
        stk = []
        ans = 0
        dp = [0] * len(A)

        for i in range(len(A)):
            while stk and A[stk[-1]] < A[i]:
                dp[i] = max(dp[stk.pop()], dp[i] + 1)
                ans = max(ans, dp[i])
            stk.append(i)
        return ans


"""
[5,3,4,4,7,3,6,11,8,5,11]
[4,5,7,7,13]
[5,14,15,2,11,5,13,15]
[10,1,2,3,4,5,6,1,2,3]
[10,6,5,10,15]
[7,14,4,14,13,2,6,13]
"""
