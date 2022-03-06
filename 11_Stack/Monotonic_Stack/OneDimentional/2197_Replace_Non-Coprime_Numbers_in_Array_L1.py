""" https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
monotonic coprime stack
while non-coprime pairs in stack then update it until all the pairs in stack are coprime
"""
class Solution:
    def replaceNonCoprimes(self, A: List[int]) -> List[int]:
        def is_coprime(x, y): return gcd(x, y) == 1
        
        stk = []
        for x in A:
            while stk and not is_coprime(stk[-1], x):
                xx = lcm(stk.pop(), x)
                x = xx
            else: stk.append(x)
        return stk