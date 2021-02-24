class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while Y>X:
            if Y%2==1: Y += 1
            else: Y //= 2
            ans += 1
        return ans + (X - Y)