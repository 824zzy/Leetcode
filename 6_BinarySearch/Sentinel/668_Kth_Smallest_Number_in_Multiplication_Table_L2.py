""" https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
In each row, the numbers X we get, are of the form - [i, 2*i, 3*i,...,k*i,...n*i], so x=mid/i
"""
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(mid):
            return sum(min(n, mid//(i+1)) for i in range(m))
        
        l, r = 1, m*n
        while l<=r:
            mid = (l+r)//2
            # count how many numbers are less then m in m*n
            if count(mid)<k: l = mid+1
            else: r = mid-1
        return l