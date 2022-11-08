""" https://leetcode.com/problems/merge-intervals/
use sweep line/difference array to find left and right end points of the interval
"""
from collections import defaultdict

def solution(A):
    cnt = defaultdict(int)
    for i, j, _ in A:
        for x in range(i, j+1):
            cnt[x] += 1
    
    rem = {(i, j): k for i, j, k in A}
    ans = 0
    for k, _ in sorted(cnt.items(), key=lambda x: -x[1]):
        if not rem: break
        _rem = {}
        flag = False
        for (i, j), _ in rem.items():
            if i<=k<=j:
                flag = True
                rem[(i, j)] -= 1
            if rem[(i, j)]: 
                _rem[(i, j)] = rem[(i, j)]

        rem = _rem
        if flag: ans += 1
    return ans


test_cases = [
    [[1,3,2], [2,5,3], [5, 6, 2]],
    [[1,3,2], [1,3,3], [1, 3, 1]]
]
for t in test_cases:
    print(solution(t))