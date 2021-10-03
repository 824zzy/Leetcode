""" check if a graph has a path from 1 to N
"""
from collections import defaultdict
def solution(N, A, B):
    e = defaultdict(dict)
    for i, j in zip(A, B):
        e[i][j] = e[j][i] = 1
        
    def dfs(i):
        if i == N: return True
        for j in e[i]:
            if j == i + 1: return dfs(j)
        return False
    return dfs(1)
            
    
N, A, B = input().split()
ans = solution(int(N), [int(a) for a in A.split(',')], [int(b) for b in B.split(',')])
print("{}".format(ans))