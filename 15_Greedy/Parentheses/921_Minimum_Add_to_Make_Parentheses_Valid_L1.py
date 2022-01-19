""" https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
similar to 2116
greedily find imbalanced parentheses through sum up not-opened parentheses and not-closed parentheses
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cl = op = 0
        for c in s:
            if c=='(': op += 1
            else: op -= 1
            
            if op<0:
                op = 0
                cl += 1
                
        return cl+op