""" L2: template
Find lower bound and upper bound then apply binary search two times
"""
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        def bs(l, r, t):
            while l<=r:
                m = (l+r)//2
                if A[m]==t: return m
                elif A[m]>t: r = m - 1
                else: l = m + 1
            return r
        
        tl, th = t-0.5, t+0.5
        a = bs(0, len(A)-1, tl)
        b = bs(0, len(A)-1, th)

        if a!=b: return [a+1, b]
        else: return [-1, -1]

# Using groupby
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        if t not in A: return [-1, -1]
        A = [[c, len(list(s))] for c, s in itertools.groupby(A)]
        ans = 0
        for c, l in A:
            if c==t: return [ans, ans+l-1]
            else: ans += l