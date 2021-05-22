# two pointer template: variance of 167
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, round(sqrt(c))
        while l<=r:
            if l**2+r**2<c: l += 1
            elif l**2+r**2>c: r -= 1
            else: return True
        return False
    
# O(k) with set
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums, i = set(), 0
        while i*i <= c:
            nums.add(i*i)
            i += 1
        for n in nums:
            if c-n in nums:
                return True
        return False
        


# O(k) without set
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        m = int(sqrt(c))
        for a in range(1, m+1):
            b = round(sqrt(c-a*a))
            if a*a+b*b == c:
                return True
        return False