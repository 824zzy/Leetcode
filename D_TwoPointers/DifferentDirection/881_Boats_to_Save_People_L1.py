""" https://leetcode.com/problems/boats-to-save-people/
1. sort people and greedily carry as much people as boat can
2. since people[i]<limit and as problem described the boat can at least carry one people and at most carry two people,
   so update right pointer when it is possible to carry two people (if A[l]+A[r]<=L: r -= 1)
"""
from header import *

class Solution:
    def numRescueBoats(self, A: List[int], L: int) -> int:
        A.sort(reverse=True)
        l, r = 0, len(A)-1
        ans = 0
        while l<=r:
            if A[l]+A[r]<=L: r -= 1
            l += 1
            ans += 1
        return ans
    

# another perspective by summarizing the condition in three cases
class Solution:
    def numRescueBoats(self, A: List[int], limit: int) -> int:
        A.sort()
        ans = 0
        l, r = 0, len(A)-1
        while l<=r:
            if A[r]+A[r-1]<=limit:
                r -= 2
            elif A[l]+A[r]<=limit:
                l += 1
                r -= 1
            elif A[r]<=limit:
                r -= 1
            ans += 1
        return ans