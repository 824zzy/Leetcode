""" https://leetcode.com/problems/summary-ranges/
use same direction two pointers by checking A[j]+1!=A[j+1]
"""
class Solution:
    def summaryRanges(self, A: List[int]) -> List[str]:
        A += [inf]
        i = 0
        ans = []
        for j in range(len(A)-1):
            if A[j]+1!=A[j+1]:
                if i==j:
                    ans.append(str(A[j]))
                else:
                    ans.append('->'.join([str(A[i]), str(A[j])]))
                i = j + 1
        return ans