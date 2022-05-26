""" https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
monotonic coprime stack
while non-coprime pairs in stack then update it until all the pairs in stack are coprime
"""
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums: 
            while stack and gcd(stack[-1], x) > 1: x = lcm(x, stack.pop())
            stack.append(x)
        return stack