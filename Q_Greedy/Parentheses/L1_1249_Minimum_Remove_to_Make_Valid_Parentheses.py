""" https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
filter string by two pass
1. forward pass to calculate how many open counts at every index
2. backward pass to calculate how many close counts at every index
3. for each index, check if their open and close counts are valid(>=0)
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op = 0
        forward = []
        for c in s:
            if c=='(': op += 1
            elif c==')': op -= 1
            forward.append(op)
            if op<0: op = 0
        
        cl = 0
        backward = []
        for c in reversed(s):
            if c==')': cl += 1
            elif c=='(': cl -= 1
            backward.append(cl)
            if cl<0: cl = 0
        
        ans = ''
        for idx, (i, j) in enumerate(zip(forward, reversed(backward))):
            if i>=0 and j>=0: ans += s[idx]
        return ans