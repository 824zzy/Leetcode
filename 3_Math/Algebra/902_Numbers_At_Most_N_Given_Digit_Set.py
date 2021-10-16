""" L2: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
"""
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], n: int) -> int:
        N = str(n)
        ans = sum(len(D)**i for i in range(1, len(N)))
        i = 0
        while i<len(str(n)):
            ans += sum(c<N[i] for c in D) * (len(D) ** (len(N)-i-1))
            if N[i] not in D: break
            i += 1
        return ans + (i==len(N))