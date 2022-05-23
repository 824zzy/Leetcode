""" https://leetcode.com/problems/daily-temperatures/submissions/
use monotonic decreasing stack to keep track of first temperature larger than stack top element.
"""
class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        stk = []
        ans = [0]*len(A)
        
        for i in range(len(A)):
            while stk and A[stk[-1]]<A[i]:
                ii = stk.pop()
                ans[ii] = i-ii
            stk.append(i)
        return ans