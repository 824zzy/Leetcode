""" https://leetcode.com/problems/add-strings/
string + simulation
"""


class Solution:
    def addStrings(self, a: str, b: str) -> str:
        a, b = list(map(int, a)), list(map(int, b))
        carry = 0
        ans = []
        while a or b:
            x = a.pop() if a else 0
            y = b.pop() if b else 0
            ans.append((x + y + carry) % 10)
            carry = (x + y + carry) // 10
        if carry:
            ans.append(carry)
        return "".join(map(str, ans[::-1]))
