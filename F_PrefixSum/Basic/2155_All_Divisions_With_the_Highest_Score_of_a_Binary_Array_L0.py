""" https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
calcualte prefix sum of 0s and 1s and find highest score by linear scan
"""
class Solution:
    def maxScoreIndices(self, A: List[int]) -> List[int]:
        prefix0, prefix1 = [0], [0]
        p0, p1 = 0, 0
        for i, j in zip(A, A[::-1]):
            if i==0: p0 += 1
            prefix0.append(p0)
            if j==1: p1 += 1
            prefix1.append(p1)
        prefix1 = prefix1[::-1]
        
        ans = defaultdict(list)
        for idx, (i, j) in enumerate(zip(prefix0, prefix1)):
            ans[i+j].append(idx)
    
        return ans[max(ans)]