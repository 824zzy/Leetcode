""" https://codeforces.com/problemset/problem/71/A
"""
def solution(w):
    if len(w)>10: return w[0]+str(len(w)-2)+w[-1]
    else: return w
        
n = int(input())
ans = []
for i in range(n):
    w = input()
    ans.append(solution(w))

for i in range(len(ans)): print(ans[i])