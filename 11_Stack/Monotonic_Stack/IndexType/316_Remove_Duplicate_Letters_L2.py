""" L2: https://leetcode.com/problems/remove-duplicate-letters/
https://leetcode.com/problems/remove-duplicate-letters/discuss/894596/Python3-stack-O(N)-time-O(N)-space
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