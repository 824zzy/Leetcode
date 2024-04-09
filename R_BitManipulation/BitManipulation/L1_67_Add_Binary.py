""" https://leetcode.com/problems/add-binary/
sum up every bits
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, carry = [], 0
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            carry, d = divmod(carry, 2)
            ans.append(d)
        if carry:
            ans.append(carry)
        return ''.join(map(str, reversed(ans)))

# cheating solution


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
