""" L1
simulate insert sort and cound number of insert
"""
import heapq
def Sorting(A):
    ans = 0
    A = [int(a) for a in A.split()]
    ans = []
    H1, H2 = [], []
    for a in A:
        if a%2: heapq.heappush(H1, a)
        else: heapq.heappush(H2, -a)
    for a in A:
        if a%2: ans.append(str(heapq.heappop(H1)))
        else: ans.append(str(-1*heapq.heappop(H2)))
    return " ".join(ans)
        
t = int(input())
for i in range(1, t+1):
    l = input()
    A = input()
    ans = Sorting(A)
    print("Case #{}: {}\n".format(i, ans), flush=True)