""" https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
"""
class Solution:
    def minimumCost(self, A: List[int]) -> int:
        A.sort(reverse=True)
        ans = 0
        for i in range(0, len(A), 3):
            if len(A[i:i+3])==3: ans += sum(A[i:i+2])
            else: ans += sum(A[i:i+3])
        return ans