""" https://leetcode.com/problems/bag-of-tokens/
1. sort the tokens first
2. greedily play the left token face up and right token face down
"""
class Solution:
    def bagOfTokensScore(self, A: List[int], p: int) -> int:
        A.sort()
        ans = 0
        l, r = 0, len(A)-1
        while l<=r:
            if p>=A[l]:
                p -= A[l]
                l += 1
                ans += 1
            elif ans>0 and l<r:
                p += A[r]
                r -= 1
                ans -= 1
            else: break
        return ans