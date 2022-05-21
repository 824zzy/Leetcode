""" https://leetcode.com/problems/tallest-billboard/
This is a special 01 knapsack that we have three choice for each item:
1. skip the rod
2. add the rod to left steel
3. add the rod to right steel

"""
class Solution:
    def tallestBillboard(self, A: List[int]) -> int:
        @cache
        def dp(i, diff):
            print(i, diff)
            if i==len(A): return 0 if diff==0 else -inf
            # skip
            ans = dp(i+1, diff)
            # add to left steel
            ans = max(ans, A[i]+dp(i+1, diff+A[i]))
            # add to right steel
            ans = max(ans, A[i]+dp(i+1, diff-A[i]))
            return ans
        
        return dp(0, 0)//2