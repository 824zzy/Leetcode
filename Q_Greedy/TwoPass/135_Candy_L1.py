""" https://leetcode.com/problems/candy/
two pass to greedily find minimal candy counts.
Note that during the second pass, we need to avoid overwriting previous results by max. E.g. : 1,3,4,5,2
"""
class Solution:
    def candy(self, A: List[int]) -> int:
        ans = [1] * len(A)
        for i in range(len(A)-1):
            if A[i]<A[i+1]:
                ans[i+1] = ans[i]+1

        for i in reversed(range(1, len(A))):
            if A[i-1]>A[i]: 
                ans[i-1] = max(ans[i]+1, ans[i-1])
        return sum(ans)