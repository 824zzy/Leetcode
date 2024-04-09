""" https://codeforces.com/problemset/problem/263/A
"""


def solution(A):
    for i in range(5):
        for j in range(5):
            if A[i][j] == '1':
                return abs(2 - i) + abs(2 - j)


A = []
for _ in range(5):
    row = input()
    A.append(row.split())

ans = solution(A)
print(ans)
