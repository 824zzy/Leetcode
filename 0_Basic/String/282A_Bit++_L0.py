""" https://codeforces.com/problemset/problem/282/A
find +/- in each line
"""
def solution(A):
    ans = 0
    for x in A:
        if x[0]=='+' or x[-1]=='+': ans += 1
        else: ans -= 1
    return ans
    
n = int(input())
ops = [input() for _ in range(n)]
ans = solution(ops)
print(ans)