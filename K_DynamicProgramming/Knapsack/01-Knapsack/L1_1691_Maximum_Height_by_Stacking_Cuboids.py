""" https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
"""
# sort and knapsack
class Solution:
    def maxHeight(self, A: List[List[int]]) -> int:
        A = [sorted(x, reverse=True) for x in A]
        A.sort(reverse=True)
        
        @cache
        def dp(i, h, l, w):
            if i==len(A): return 0
            hh, ll, ww = A[i]
            if hh<=h and ll<=l and ww<=w:
                return max(hh+dp(i+1, hh, ll, ww), dp(i+1, h, l, w))
            else:
                return dp(i+1, h, l, w)
        
        return dp(0, inf, inf, inf)


# check all the available cuboids
class Solution:
    def maxHeight(self, A: List[List[int]]) -> int:
        A = [sorted(x, reverse=True) for x in A]
        A.sort(reverse=True)

        @cache
        def dp(i):
            if i==len(A)-1: return A[i][0]
            ans = A[i][0]
            for j in range(i+1, len(A)):
                if A[i][1]>=A[j][1] and A[i][2]>=A[j][2]:
                    ans = max(ans, A[i][0]+dp(j))
            return ans
        
        return max([dp(i) for i in range(len(A))])