""" https://foobar.withgoogle.com/free_the_bunny_workers
1. count the least necessary identical keys by n-r+1.
2. distribute the keys to bunnies by combiantions
"""
from itertools import combinations

def solution(n, r):
    key_cnts = n-r+1
    ans = [[] for _ in range(n)]
    for k, v in enumerate(combinations([i for i in range(n)], key_cnts)):
        for i in v: 
            ans[i].append(k)
    return ans


# ans = solution(5, 3)
# print(ans)