""" https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
1. create a fixed window which size is ones' count.
2. minimum swaps is the zeros' count in the fixed window

"""
class Solution:
    def minSwaps(self, A: List[int]) -> int:
        cnt1 = A.count(1)
        ans = inf
        cnt0 = 0
        A *= 2
        
        for i in range(len(A)):
            if A[i]==0: cnt0 += 1
            if i>=cnt1 and A[i-cnt1]==0: cnt0 -= 1
            if i>=cnt1: ans = min(ans, cnt0)
        return ans


# suboptimal dynamic window solution
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