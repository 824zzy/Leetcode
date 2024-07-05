""" https://leetcode.com/problems/capitalize-the-title/
"""


class Solution:
    def capitalizeTitle(self, A: str) -> str:
        def fn(x):
            if len(x) <= 2:
                return x.lower()
            else:
                return x[0].upper() + x[1:].lower()  # x.title()

        return " ".join(map(fn, A.split()))
