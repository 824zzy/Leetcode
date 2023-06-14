""" https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
1. binary search
2. greedily fill the array
3. calculate the sum by the summation formula
"""
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def fn(x):
            l, r = index+1, n-index
            if l>x:
                lSum = x*(x+1)/2+(l-x)
            else:
                lSum = l*x+l*(l-1)*(-1)/2
            if r>x:
                rSum = x*(x+1)/2+(r-x)
            else:
                rSum = r*x+r*(r-1)*(-1)/2
            return lSum+rSum-x>maxSum
            
            
        l, r = 0, maxSum+1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l-1
        
        
        
"""
4
2
6
6
1
10
3
2
18
8
7
14
4
0
4
"""