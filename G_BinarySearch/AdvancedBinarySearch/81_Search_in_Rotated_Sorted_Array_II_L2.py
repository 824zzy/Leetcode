""" https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
If the number in the middle is less than the rightmost number, the right half is ordered;
If the middle number is greater than the rightmost number, the left half is ordered.
Else if the middle number is equal to rightmost number, the right pointer should minus one.
"""
class Solution:
    def search(self, A: List[int], t: int) -> bool:
        l, r = 0, len(A)-1
        while l<=r:
            m = (l+r)//2
            if A[m]==t:
                return True
            elif A[m]<A[r]:
                if A[m]<t<=A[r]: l = m + 1
                else: r = m - 1 
            elif A[m]>A[r]:
                if A[l]<=t<A[m]: r = m - 1
                else: l = m + 1
            else: r -= 1
        return False