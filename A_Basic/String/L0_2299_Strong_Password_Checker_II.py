""" https://leetcode.com/problems/strong-password-checker-ii/
simulate the password check by a few booleans
"""


class Solution:
    def strongPasswordCheckerII(self, A: str) -> bool:
        if len(A) < 8:
            return False
        has_low, has_upper, has_digit, has_special = False, False, False, False
        special = set("!@#$%^&*()-+")
        digits = set('12343567890')
        for i, c in enumerate(A):
            if c.islower():
                has_low = True
            if c.isupper():
                has_upper = True
            if c in digits:
                has_digit = True
            if c in special:
                has_special = True
            if i > 0 and A[i] == A[i - 1]:
                return False
        return has_low and has_upper and has_digit and has_special
