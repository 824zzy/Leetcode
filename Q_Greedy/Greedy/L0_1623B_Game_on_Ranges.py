""" https://codeforces.com/contest/1623/problem/B
sort the array by differences and greedily find possible x
"""


def solution(A):
    A.sort(key=lambda x: x[1] - x[0])
    ans = []
    seen = [0] * (len(A) + 1)
    for i, j in A:
        if i == j:
            seen[i] = True
            ans.append(" ".join(map(str, [i, i, i])))
        else:
            for x in range(i, j + 1):
                if not seen[x]:
                    seen[x] = True
                    ans.append(" ".join(map(str, [i, j, x])))
                    break
    return ans


N = int(input())

ans = []
for i in range(N):
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    ans.append(solution(A))

for i in range(len(ans)):
    for j in ans[i]:
        print(j)
    # print(ans[i])
