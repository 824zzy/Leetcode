""" https://codeforces.com/contest/1623/problem/A
simulate robot movings
"""
def solution(A):
    m, n, x, y, rd, cd = A
    
    dx, dy = 1, 1
    ans = 0
    t = 10
    while x!=rd and y!=cd:
        if not (1<=x+dx<=m and 1<=y+dy<=n):
            if x+dx==(m+1) or y+dy<1: dx *= -1
            if y+dy==(n+1) or x+dx<1: dy *= -1
        x, y = x+dx, y+dy
        ans += 1
    return ans
    
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(n):
    ans.append(solution(A[i]))

for i in range(len(ans)): print(ans[i])