""" https://codeforces.com/problemset/problem/1623/C
"""


def solution(A):
    def check(m):
        _A = A.copy()
        for j in range(len(A) - 1, -1, -1):
            t = min(_A[j] - m, A[j])
            if t < 0:
                return False
            if t < 3:
                continue
            if j < 2:
                continue
            _A[j - 1] += t // 3
            _A[j - 2] += t // 3 * 2
            _A[j] -= t // 3 * 3
        return True

    l, r = 0, max(A) + 1
    while l < r:
        m = (l + r) // 2
        if check(m):
            l = m + 1
        else:
            r = m
    return l - 1


N = int(input())

ans = []
for i in range(N):
    _ = int(input())
    A = list(map(int, input().split()))
    ans.append(solution(A))

for i in range(len(ans)):
    print(ans[i])
