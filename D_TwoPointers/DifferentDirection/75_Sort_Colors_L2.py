""" https://leetcode.com/problems/sort-colors/
https://leetcode.com/problems/sort-colors/discuss/681526/Python-O(n)-3-pointers-in-place-approach-explained
two methods:
    1. three pointers(dutch national flag problem)
    2. two passes by two pointers
"""
# dijkstra's dutch national flag problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class Solution:
    def sortColors(self, A: List[int]) -> None:
        i, j, k = 0, 0, len(A)-1
        while j<=k:
            if A[j]<1:
                A[i], A[j] = A[j], A[i]
                i, j = i+1, j+1
            elif A[j]>1:
                A[j], A[k] = A[k], A[j]
                k -= 1
            else: j += 1    
            
# two pass for corner cases: 1,0,1; 1,2,1
class Solution:
    def sortColors(self, A: List[int]) -> None:
        
        l, r = 0, len(A)-1
        while l<r:
            if A[l]>A[r]:
                A[l], A[r] = A[r], A[l]
            if A[l]==0: l += 1
            if A[r]==2: r -= 1
            if A[l]==A[r]:
                l += 1
        l, r = 0, len(A)-1
        while l<r:
            if A[l]>A[r]:
                A[l], A[r] = A[r], A[l]
            if A[l]==0: l += 1
            if A[r]==2: r -= 1
            if A[l]==A[r]:
                r -= 1