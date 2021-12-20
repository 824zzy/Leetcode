""" https://leetcode.com/problems/maximum-score-of-a-good-subarray/
greedily find maximum score by two pointers
"""
class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        ans = w = A[k]
        l = r = k
        while 0<=l-1 or r+1<len(A):
            if l==0 or r+1<len(A) and A[l-1]<A[r+1]:
                r += 1
                w = min(w, A[r])
            else:
                l -= 1
                w = min(w, A[l])
            ans = max(ans, w*(r-l+1))
        return ans