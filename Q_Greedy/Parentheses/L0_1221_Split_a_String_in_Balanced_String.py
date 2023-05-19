""" https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        op = 0
        ans = 0
        for c in s:
            if c=='L': op += 1
            else: op -= 1
                
            if op==0: ans += 1
        return ans