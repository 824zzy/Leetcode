""" https://leetcode.com/problems/boats-to-save-people/
1. sort people and greedily carry as much people as boat can
2. since people[i]<limit and as problem described the boat can at least carry one people and at most carry two people,
   so update right pointer when it is possible to carry two people (if A[l]+A[r]<=L: r -= 1)
"""
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