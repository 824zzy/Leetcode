""" https://foobar.withgoogle.com/doomsday_fuel
compute the limiting matrices of absorbing markov chain

Reference: 
1. Youtube tutorial: https://www.youtube.com/watch?v=qhnFHnLkrfA
2. Shrey Shah's blog: https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html
"""
from __future__  import division
from fractions import Fraction
import numpy as np
from functools import reduce

def solution(A):
    if len(A)==1: return [1, 1]
    # convert elements to probablity
    A = [[x/sum(row) if sum(row) else 0 for x in row] for row in A]
    
    # find absorbing state
    absorbing = [i for i, x in enumerate(A) if not sum(x)]
    non_absorbing = [i for i, x in enumerate(A) if sum(x)]
    
    # rearrange matrix to [I, O, R, Q] and compute F and FR
    A = np.array(A)
    Q = A[np.ix_(non_absorbing, non_absorbing)]
    R = A[np.ix_(non_absorbing, absorbing)]
    I = np.identity(len(Q))
    F = np.linalg.inv(np.subtract(I, Q))
    FR = np.dot(F, R)
    
    # format answer
    numers = [Fraction(x).limit_denominator().numerator for x in FR[0]]
    denoms = [Fraction(x).limit_denominator().denominator for x in FR[0]]
    LCM = reduce(np.lcm, denoms)
    ans = [x*LCM//y for x, y in zip(numers, denoms)]+[LCM]
    return ans


# ans = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
ans = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
print(ans)