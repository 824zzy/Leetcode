""" https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/
1. Find the minimum and maximum elements as boundary, and binary search the answer
2. The fn(x) counts how many elements less or equal than x by another binary search

Time complexity: O(m*logn*k), where fn(x) accounts for m*logn, and the outer binary search accounts for k and k=log(10^6)
"""
from header import *

class Solution:
    def matrixMedian(self, A: List[List[int]]) -> int:
        def fn(x):
            cnt = 0
            for row in A:
                cnt += bisect_right(row, x)
            return cnt
            
        m, n = len(A), len(A[0])
        target = (m*n)//2
        
        l, r = min(list(zip(*A))[0]), max(list(zip(*A))[-1])+1
        while l<r:
            mid = (l+r)//2
            if fn(mid)>target: r = mid
            else: l = mid+1
        return l
    
    
"""
[[1,1,2],[2,3,3],[1,3,4]]
[[1,1,3,3,4]]
[[71575,109387,113328,258018,317748,327741,385646,423299,489324,563784,612475,725022,728067,750414,769846,824496,899884],[19324,36317,61462,112157,286730,300583,313241,345757,483842,586927,733078,743581,752183,774762,871565,944784,956649],[2165,63036,66552,186476,217978,235978,265673,315636,328790,417180,442602,557679,566878,598316,614081,813774,969910]]
"""