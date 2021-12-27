""" L1
move left pointer when k=0 and move one step further.
"""
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        i = 0
        ans = 0
        for j in range(len(A)):
            if A[j]==0:
                if k==0:
                    while A[i]!=0: i += 1
                    i += 1
                else: k -= 1
            ans = max(ans, j-i+1)
        return ans

# another solution with the same idea
class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        ans = 0
        i = 0
        for j in range(len(A)):
            if A[j]==0:
                k -= 1
                if k<0:
                    if A[i]==0: k + 1
                    while A[i]==1: i += 1
                    i += 1
            ans = max(ans, j-i+1)
        return ans