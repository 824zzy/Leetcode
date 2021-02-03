# bit manipulation
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

# pythonic
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')