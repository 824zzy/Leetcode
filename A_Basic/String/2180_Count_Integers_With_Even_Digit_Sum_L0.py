""" https://leetcode.com/problems/count-integers-with-even-digit-sum/
brute-force count legit sum
"""
class Solution:
    def countEven(self, num: int) -> int:
        ans = 0 
        for x in range(1, num+1): 
            sm = sum(map(int, str(x)))
            if not sm&1: ans += 1
        return ans