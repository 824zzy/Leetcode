# Straight forward solution
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i**2<num:
            if i**2!=num: i += 1
        return i**2==num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l<=r:
            m = (l+r)//2
            if m**2==num: return True
            elif m**2<num: l = m + 1
            else: r = m - 1
        return False