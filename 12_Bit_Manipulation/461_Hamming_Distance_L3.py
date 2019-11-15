""" straightforward and buildtin function
zfill(n): padding zero in the front
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y, ans = bin(x)[2:], bin(y)[2:], 0
        l = max(len(x), len(y))
        x, y = x.zfill(l), y.zfill(l)
        for i in range(l):
            if x[i]!=y[i]:
                ans += 1
        return ans

# Facebook
""" bit-manipulation trick
"""
class Solution:
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')


""" basic answer
"""
class Solution(object):
    def hammingDistance(self, x, y):
        ans = 0
        while x or y:
            ans = ans + (x%2 ^ y%2)
            x = x / 2 # x >> 1
            y = y / 2 # y >> 1
        return ans