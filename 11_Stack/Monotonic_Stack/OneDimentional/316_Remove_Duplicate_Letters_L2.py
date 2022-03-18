""" https://leetcode.com/problems/remove-duplicate-letters/
1. maintain a monotonic increasing stack
2. avoid duplicates by check if character has already in stack
2. make sure the stack top character is not the last character in s by mp[stk[-1]]>i 
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mp = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s): 
            if c not in stack: 
                while stack and c < stack[-1] and i < mp[stack[-1]]: stack.pop()
                stack.append(c)
        return "".join(map(str, stack))