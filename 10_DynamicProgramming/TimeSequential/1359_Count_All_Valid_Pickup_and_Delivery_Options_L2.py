""" 
nice explanation: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516951/C%2B%2BJava-Simple-Math-Formula-with-Explanation
hard to find patterns: use combinations of all legit position
"""
class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        def dp(n):
            if n==1: return 1
            return (2*n-1)*(2*n)//2*dp(n-1)
        return dp(n)%(10**9+7)