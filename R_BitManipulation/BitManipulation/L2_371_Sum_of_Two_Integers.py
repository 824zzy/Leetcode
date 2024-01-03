""" https://leetcode.com/problems/sum-of-two-integers/submissions/
1. bitwise xor to add two numbers bit by bit,
2. bitwise and to calculate the carry
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b&mask:
            carry = a&b
            a = a^b
            b = carry<<1
        return a&mask if b>mask else a