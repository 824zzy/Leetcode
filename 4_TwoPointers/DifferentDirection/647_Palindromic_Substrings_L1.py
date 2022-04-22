""" https://leetcode.com/problems/palindromic-substrings/
the same as 5

lo = i//2, hi = (i+1)//2 to cover odd and even cases
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2*len(s)-1):
            lo = i//2
            hi = (i+1)//2
            while 0 <= lo <= hi < len(s) and s[lo] == s[hi]: 
                ans += 1
                lo, hi = lo-1, hi+1
        return ans 