""" https://leetcode.com/problems/get-equal-substrings-within-budget/
1. build the difference array
2. use sliding window template
"""
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        A = [abs(ord(ss)-ord(tt)) for ss, tt in zip(s, t)]
        i = 0
        ans = 0
        cost = 0
        
        for j in range(len(A)):
            cost += A[j]
            while cost>maxCost:
                cost -= A[i]
                i += 1
            ans = max(ans, j-i+1)
        return ans