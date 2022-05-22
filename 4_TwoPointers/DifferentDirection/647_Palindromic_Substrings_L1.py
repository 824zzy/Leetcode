""" https://leetcode.com/problems/palindromic-substrings/
the same as 5

1. l = i//2, r= (i+1)//2 to cover odd and even cases
2. expand left and right point from middle to sides
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2*len(s)-1):
            l, r = i//2, (i+1)//2
            while 0<=l<=r<len(s) and s[l]==s[r]:
                ans += 1
                l, r = l-1, r+1
                
        return ans