""" L2: complicated but not hard simulation
"""


def super2048(A, D):
    M, N = len(A), len(A[0])
    if D == "right":
        A = [[e for e in row[::-1] if e != 0] for row in A]
    if D == "left":
        A = [[e for e in row if e != 0] for row in A]
    if D == "up":
        A = [[e for e in list(column) if e != 0] for column in zip(*A)]
    if D == "down":
        A = [[e for e in list(column)[::-1] if e != 0] for column in zip(*A)]
    tmp = []
    for row in A:
        new_r = []
        while row:
            cur = row.pop(0)
            if cur != 0:
                if row and row[0] == cur:
                    row.pop(0)
                    new_r.append(cur * 2)
                else:
                    new_r.append(cur)
        tmp.append(new_r)
    ans = []
    if D == "right":
        for row in tmp:
            row.extend([0] * (N - len(row)))
            ans.append(row[::-1])
    if D == "left":
        for row in tmp:
            row.extend([0] * (N - len(row)))
            ans.append(row)
    if D == "up":
        for row in tmp:
            row.extend([0] * (M - len(row)))
            ans.append(row)
        ans = [list(row) for row in zip(*ans)]
    if D == "down":
        for row in tmp:
            row.extend([0] * (M - len(row)))
            ans.append(row)
        ans = [list(row) for row in zip(*ans)]
        ans = ans[::-1]
    return ans


t = int(input())
for i in range(1, t + 1):
    n, D = input().split()
    A = []
    for _ in range(int(n)):
        A.append(list(map(int, input().split())))
    ans = super2048(A, D)
    print("Case #{}:".format(i))
    for row in ans:
        print(" ".join([str(e) for e in row]))
