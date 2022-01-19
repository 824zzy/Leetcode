""" https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
steal from god ye: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/1073138/Python3-stack
Use a stack to collect the locations of (. Whenever seeing a ), we pop out a ( if we can. Otherwise, remove the ). In the end, remove all (s left.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s): 
            if c == "(": stack.append(i)
            elif c == ")": 
                if stack: stack.pop() # matching 
                else: s[i] = "" # extra 
        while stack: s[stack.pop()] = ""
        return "".join(s)