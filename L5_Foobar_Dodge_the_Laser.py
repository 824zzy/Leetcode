from header import *

def solution(A):
    # Kadane's algorithm
    mn = inf
    ans = -inf
    for p in A:
        mn = min(mn, p)
        ans = max(ans, p-mn)
    return ans if ans!=-inf else -1


A = input()
A = [int(x) for x in A.split()]
ans = solution(A)
print(ans)


"""
"""