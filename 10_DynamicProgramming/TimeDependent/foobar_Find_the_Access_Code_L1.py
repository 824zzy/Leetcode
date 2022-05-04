""" https://foobar.withgoogle.com/find-the-access-code
1. dp solution
2. hash table solution
"""
from collections import Counter
from functools import cache

def solution(A):
    @cache
    def dp(i, k):
        if k==3: return 1
        if i==len(A): return 0
        ans = 0
        for j in range(i+1, len(A)):
            if A[j]%A[i]==0:
                ans += dp(j, k+1)
        return ans
    return dp(0, 1)


def solution(A):
    ans = 0
    cnt = Counter()
    for i in range(len(A)):
        for j in range(i):
            if A[i]%A[j]==0:
                cnt[i] += 1
                ans += cnt[j]
    return ans
        
