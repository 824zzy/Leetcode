""" L1: https://leetcode.com/problems/3sum-closest/
repeated two sum by two pointers.
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

# less optimal
class Solution:
    def threeSumClosest(self, A: List[int], t: int) -> int:
        A.sort()
        ans = float('inf')
        for i in range(len(A)):
            l, r = i+1, len(A)-1
            while l<r:
                cur_s = A[i]+A[l]+A[r]
                if cur_s-t>0: r -= 1
                elif cur_s-t<0: l += 1
                else:
                    l += 1
                    while l<r and A[l-1]==A[l]: l += 1
                ans = min(ans, cur_s, key=lambda x: abs(t-x))
        return ans