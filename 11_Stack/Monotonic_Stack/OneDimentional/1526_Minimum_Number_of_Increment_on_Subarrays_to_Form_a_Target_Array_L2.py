""" https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
from ye: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/1105152/Python3-mono-stack
"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0 
        stack = [] # increasing stack
        for x in target: 
            while stack and stack[-1] >= x: 
                ans += stack.pop() - max(x, (stack or [0])[-1])
            stack.append(x)
            
        prev = 0
        for x in stack: 
            ans += x - prev 
            prev = x
        return ans