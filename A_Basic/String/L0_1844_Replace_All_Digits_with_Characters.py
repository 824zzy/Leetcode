""" https://leetcode.com/problems/replace-all-digits-with-characters/
integer to character
"""


class Solution:
    def replaceDigits(self, A: str) -> str:
        ans = ""
        for i in range(len(A)):
            if i % 2 == 0:
                ans += A[i]
            else:
                ans += chr(ord(ans[i - 1]) + int(A[i]))
        return ans
