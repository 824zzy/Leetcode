""" https://leetcode.com/problems/3sum-closest/
sort A and greedily find minimum three sum by two pointers.
"""
# optimal
class Solution:
    def threeSumClosest(self, A: List[int], t: int) -> int:
        A.sort()
        ans = float('inf')
        for i in range(len(A)):
            if i and A[i-1] == A[i]: continue
            l, r = i+1, len(A)-1
            while l<r:
                cur_s = A[i]+A[l]+A[r]
                ans = min(ans, cur_s, key=lambda x: abs(t-x))
                if cur_s>t: r -= 1
                elif cur_s<t: l += 1
                else: return ans
                
        return ans