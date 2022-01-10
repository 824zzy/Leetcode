""" https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
count zeros in a fixed window which size is ones' count.
"""
class Solution:
    def minSwaps(self, A: List[int]) -> int:
        ones = A.count(1)
        A *= 2
        ans = inf 
        cnt = 0
        i = 0
        for j in range(len(A)):
            cnt += A[j]
            if j>=ones: 
                cnt -= A[i]
                i += 1
            ans = min(ans, ones-cnt)
        return ans
    
class Solution:
    def minSwaps(self, A: List[int]) -> int:
        if all(A) or not any(A): return 0
        ones = A.count(1)
        A = A*2
        i = 0
        cnt = 0
        ans = inf
        for j in range(i, len(A)):
            if A[j]==0: cnt += 1
            if j-i+1==ones:
                ans = min(ans, cnt)
                if A[i]==1: i += 1
                else:
                    while i<len(A) and A[i]==0: 
                        i += 1
                        cnt -= 1
        return ans