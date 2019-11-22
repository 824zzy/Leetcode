class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l<=r:
            m = (l+r)//2
            # print(l, r, m)
            if m*m==x:
                return m
            elif m*m>x:
                r = m - 1
            else:
                l = m + 1
        # print(l, r, m)
        return r