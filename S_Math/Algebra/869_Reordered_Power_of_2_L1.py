""" Counter
Just counter the number of digits in the given number,
rather than permutation
"""
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        cand = [Counter(str(2**i)) for i in range(30)]
        for c in cand:
            if Counter(str(N))==c: return True
        return False

""" Straight forward permutation
Calculate all the permutations of given number
"""
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        cand = itertools.permutations(str(N))
        for c in cand:
            if c[0]!='0':
                n = int(''.join(c))
                while n%2==0: n /= 2
                if n==1: return True
        return False