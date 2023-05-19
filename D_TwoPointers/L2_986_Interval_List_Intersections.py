""" https://leetcode.com/problems/interval-list-intersections/
Define two pointers to scan through A and B respectively. If the intervals overlap, put the overlapped part in ans. 
Otherwise, increment the pointer for the interval that ends ahead.
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        ans = []
        while l<len(A) and r<len(B):
            maxL = max(A[l][0], B[r][0])
            minR = min(A[l][1], B[r][1])
            if maxL<=minR: ans.append([maxL, minR])
            if A[l][1]<B[r][1]: l += 1
            else: r += 1
        return ans