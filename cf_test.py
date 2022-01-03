def solution(A):
    t = min(A[0], A[1])
    for i in range(2, len(A)):
        x = A[i]//3
        A[i] -= 3*x
        A[i-1] += x
        A[i-2] += 2*x
    print("dada", A)
    return min(A)

N = int(input())

ans = []
for i in range(N):
    _ = int(input())
    A = list(map(int, input().split()))
    ans.append(solution(A))

for i in range(len(ans)): 
    print(ans[i])