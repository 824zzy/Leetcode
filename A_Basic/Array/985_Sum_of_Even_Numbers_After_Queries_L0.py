""" https://leetcode.com/problems/sum-of-even-numbers-after-queries/
simulation
"""
from header import *

class Solution:
    def sumEvenAfterQueries(self, A: List[int], Q: List[List[int]]) -> List[int]:
        even_sm = sum(x for x in A if not x&1)
        
        ans = []
        for v, i in Q:
            # if A[i] is odd
            if A[i]&1:
                A[i] += v
                # if new A[i] becomes even, then add new A[i] to sum
                if not A[i]&1:
                    even_sm += A[i]
            # if A[i] is even
            else:
                tmp = A[i]
                A[i] += v
                # if new A[i] still even, then add v to sum
                if not A[i]&1:
                    even_sm += v
                # if new A[i] becomes odd, then remove A[i] from sum
                else:
                    even_sm -= tmp
            ans.append(even_sm)
        return ans
    
    
# optimal official solution: remove A[index] from S if it is even, then add A[index] + val back (if it is even.)
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)

        return ans