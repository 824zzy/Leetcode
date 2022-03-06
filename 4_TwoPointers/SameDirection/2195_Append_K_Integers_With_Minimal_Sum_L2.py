""" https://leetcode.com/problems/append-k-integers-with-minimal-sum/
TODO: learn thinking reversely from ye15's solution: https://leetcode.com/problems/append-k-integers-with-minimal-sum/discuss/1823628/Python3-swap
"""
class Solution:
    def minimalKSum(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 0
        i = 0
        for j in range(len(A)):
            if A[j]>i:
                d = min(k, A[j]-i-1)
                k -= d
                ans += (i+1+i+d)*d//2
                i = A[j]
            if k==0: return ans
        if k: ans += (A[-1]+A[-1]+k+1)*k//2
        return ans
    

# ye15 solution
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k*(k+1)//2
        prev = -inf 
        for x in sorted(nums): 
            if prev < x: 
                if x <= k: 
                    k += 1
                    ans += k - x
                else: break
                prev = x
        return ans 