""" https://codeforces.com/problemset/problem/4/A
w has to be even number and larger than 2
"""
def solution(w):
    return w&1==0 and w>2
        
w = int(input())
ans = solution(w)
if ans==1: print("YES")
else: print("NO")