""" https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
case 1: N has n digits, so all numbers less than n digits are valid, which are: sum(len(D) ** i for i in range(1, n))
case 2: deal with all numbers with n digits
"""
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        N = str(N)
        # case1
        ans = sum(len(D)**i for i in range(1, len(N))) 
        # case 2
        for i, c in enumerate(N):
            ans += sum(c<N[i] for c in D) * (len(D)**(len(N)-i-1))
            if c not in D: return ans
        return ans + 1
