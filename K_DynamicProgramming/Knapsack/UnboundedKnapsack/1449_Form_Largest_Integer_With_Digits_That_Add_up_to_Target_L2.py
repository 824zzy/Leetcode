""" https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
It is L2 due to the large target value constraint:
1. 'dp(n-c)*10+d': works
2. 'd*10**i+dp(i+1, n-c)': Error(OverflowError: int too large to convert to float)
"""
class Solution:
    def largestNumber(self, A: List[int], target: int) -> str:
        A = {i: A[i-1] for i in range(1, len(A)+1)}
        
        @cache
        def dp(n):
            if n<0: return -inf
            elif n==0: return 0
            
            ans = -inf
            for d, c in A.items():
                ans = max(ans, dp(n-c)*10+d)
            return ans
        
        ans = dp(target)
        return str(ans) if ans!=-inf else str('0')