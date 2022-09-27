""" https://leetcode.com/problems/minimum-money-required-before-transactions/
1. greedily sort the transactions by: 
    - For transactions that have cashback greater or equal to cost, sort them by cost in descending order.
    - For transactions that have cashback less than cost, sort them by cashback in descending order.
2. use binary search to find the minimum money required before transactions. Note that the upper bound of the money required is 10**14+1.
"""
from header import *

class Solution:
    def minimumMoney(self, A: List[List[int]]) -> int:
        _A1 = sorted([[x, y] for x, y in A if x<=y], key=lambda xx: -xx[0])
        _A2 = sorted([[x, y] for x, y in A if x>y], key=lambda xx: xx[1])
        A = _A2+_A1
        
        def fn(m):
            for c, cb in A:
                if m<c: return False
                m = m-c+cb
            return True
        
        
        ans = 0
        l, r = 0, 10**14+1
        while l<r:
            m = (l+r)//2
            if fn(m): r = m
            else: l = m+1
        return l
                

"""
[[2,1],[5,0],[4,2]]
[[3,0],[0,3]]
[[3,9],[0,4],[7,10],[3,5],[0,9],[9,3],[7,4],[0,0],[3,3],[8,0]]
[[4,10],[4,8],[7,10],[6,5]]
[[91,38],[79,43],[45,5],[46,1],[6,80],[51,5],[16,88],[53,99],[46,32],[29,38],[9,42],[53,77],[13,62],[76,10],[1,36],[33,73],[97,19],[12,8],[39,25],[90,54],[23,64],[21,43],[20,67],[16,22],[59,46],[64,55],[4,30],[53,100],[9,31],[41,100],[19,21],[6,20],[49,92],[54,32],[91,36],[63,30],[86,25],[2,81],[54,42],[37,38],[93,95],[87,34],[6,12],[84,73],[12,5],[39,98],[50,89],[28,35],[75,77],[7,72],[30,17],[34,7],[39,98],[61,39],[0,82],[87,13],[18,16],[37,76]]
"""