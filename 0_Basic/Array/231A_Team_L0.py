""" https://codeforces.com/problemset/problem/231/A
"""
def solution(A):
    return sum(A)>=2
    
n = int(input())
ans = 0
for i in range(n):
    A = list(map(int, input().split()))
    ans += solution(A)

print(ans)