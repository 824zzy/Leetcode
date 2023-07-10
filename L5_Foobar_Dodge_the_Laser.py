from header import *

def maxHeight(wallPositions, wallHeights):
    # adjacent walls: skip
    # has n space
    #   the two walls height difference is larger than n+1 ==> ans = min(l, r)+n
    #   if the two walls height difference == n+1, ans = max(l, r)-1
    #   if the two walls height difference == 0 ==> ans = x+ceil(n/2)
    #   else: binary search the answer
    def fn(lh, rh, m, n):
        m_r = n-m
        if lh+m<=rh+m_r: return False
        else: return True
        
    A = sorted(zip(wallPositions, wallHeights))
    ans = 0
    for i in range(len(A)-1):
        lp, lh = A[i]
        rp, rh = A[i+1]
        n = rp-lp-1
        if lh>rh:
            lp, lh, rp, rh = rp, rh, lp, lh
            n = lp-rp-1
        if abs(lp-rp)==1: continue
        if lh==rh: 
            ans = max(ans, lh+ceil(n)/2)
            continue
        if abs(rh-lh)>n+1: ans = max(ans, min(lh, rh)+n)
        l, r = 0, n+2
        while l<r:
            m = (l+r)//2
            print(m, fn(lh, rh, m, n))
            if fn(lh, rh, m, n): r = m
            else: l = m+1
        ans = max(ans, lh+l-1)
    return ans
        
        
        






A = input()
A = [int(x) for x in A.split()]
B = input()
B = [int(x) for x in B.split()]
ans = maxHeight(A, B)
print(ans)


"""
"""