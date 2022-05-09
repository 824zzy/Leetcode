""" https://foobar.withgoogle.com/doomsday_fuel
compute the limiting matrices of absorbing markov chain

Reference: 
1. Youtube tutorial: https://www.youtube.com/watch?v=qhnFHnLkrfA
2. Shrey Shah's blog: https://pages.cs.wisc.edu/~shrey/2020/08/10/google-foobar.html
"""
from itertools import groupby
def largestGoodInteger(num):
    A = [[k, len(list(v))] for k, v in groupby(num)]
    ans = ''
    print(A)
    for k, v in A:
        if v==3: ans = max(ans, k*v)
    return ans


ans = largestGoodInteger("74444")
print(ans)