""" https://codeforces.com/problemset/problem/50/A
greedily find maximum piling numbers
"""


def solution(M, N):
    return M * N // 2


M, N = list(map(int, input().split()))
ans = solution(M, N)
print(ans)
