""" https://codeforces.com/problemset/problem/71/A
negative's remainder will round down: -20%60 = 40
"""
def solution(A, k):
    t = A[k-1]
    ans = 0
    for i in range(len(A)):
        if A[i]>=t and A[i]>0: ans += 1
    return ans
    
    
n, k = input().split()
n, k = int(n), int(k)
A = list(map(int, input().split()))
ans = solution(A, k)
print(ans)