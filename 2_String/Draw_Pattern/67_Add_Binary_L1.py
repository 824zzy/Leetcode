# Facebook
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

# Stack
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, carry = "", 0
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            ans = str(carry%2)+ans
            carry //= 2
        return ans
        