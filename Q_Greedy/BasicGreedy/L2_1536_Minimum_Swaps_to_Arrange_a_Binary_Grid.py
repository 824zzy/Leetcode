""" https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
summarizing row into number and sequentially find row to fill in
"""
class Solution:
    def minSwaps(self, A: List[List[int]]) -> int:
        # summarizing row into number
        row = [0]*len(A)
        for i in range(len(A)):
            for j in reversed(range(len(A))):
                if A[i][j]: 
                    row[i] = j
                    break
        
        ans = 0
        # sequentially find row to fill in
        for k in range(len(A)):
            for i, v in enumerate(row):
                if v<=k:
                    ans += i
                    row.pop(i)
                    break
            else: return -1
        return ans