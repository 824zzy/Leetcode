""" https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
compare bit by bit
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            _a = a & 1 if a else 0
            _b = b & 1 if b else 0
            _c = c & 1 if c else 0
            if _c == 0:
                if _a == 1 and _b == 1:
                    ans += 2
                elif _a == 1 or _b == 1:
                    ans += 1
            elif _c == 1:
                if _a == 0 and _b == 0:
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


# solution from ye using divmod
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        while a or b or c:
            a, aa = divmod(a, 2)
            b, bb = divmod(b, 2)
            c, cc = divmod(c, 2)
            if cc == 1:
                ans += (aa == bb == 0)
            else:
                ans += (aa == 1) + (bb == 1)
        return ans
