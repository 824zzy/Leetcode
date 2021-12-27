""" L2: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
Find lower bound and upper bound by bisect
"""
# bisect
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        l = bisect_left(A, t)
        r = bisect_right(A, t)-1
        
        if r>=0 and l<len(A) and A[l]==t and A[r]==t: return [l, r]
        else: return [-1, -1]

# groupby func
class Solution:
    def searchRange(self, A: List[int], t: int) -> List[int]:
        if t not in A: return [-1, -1]
        A = [[c, len(list(s))] for c, s in itertools.groupby(A)]
        ans = 0
        for c, l in A:
            if c==t: return [ans, ans+l-1]
            else: ans += l