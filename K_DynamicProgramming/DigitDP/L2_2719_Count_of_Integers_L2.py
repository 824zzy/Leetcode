""" https://leetcode.com/problems/count-of-integers/
"""
from header import *
    
class Solution:
    def count(self, n1: str, n2: str, mn: int, mx: int) -> int:
        MOD = 10**9+7
        def f(s):
            @cache
            def dp(i, sm, is_limit):
                if sm>mx:
                    return 0
                if i==len(s):
                    return sm>=mn
                ans = 0
                up = int(s[i]) if is_limit else 9
                for j in range(up+1):
                    ans += dp(i+1, sm+j, is_limit and j==up)
                return ans%MOD
            return dp(0, 0, True)
        return f(n2)-f(n1)+(mn<=sum(map(int, n1))<=mx)
    
"""
"1"
"12"
1
8
"1"
"5"
1
5
"1000000007"
"2000000014"
1
400
"""