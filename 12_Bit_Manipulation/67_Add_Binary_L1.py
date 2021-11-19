""" https://leetcode.com/problems/add-binary/
use `zip_longest`
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, carry = [], 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            carry += (x=='1')+(y=='1')
            carry, d = divmod(carry, 2)
            ans.append(d)
        if carry: ans.append(carry)
        return ''.join(map(str, reversed(ans)))

# cheating solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]