class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m!=n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift