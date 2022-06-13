"""L1: Template problem
Use s to increase/decrease duplicated value for optimizing performance
"""
class Solution:
    def maximumUniqueSubarray(self, A: List[int]) -> int:
        i, ans, s, win = 0, A[0], A[0], set([A[0]])
        for j in range(1, len(A)):
            while A[j] in win: 
                win.remove(A[i])
                s -= A[i]
                i += 1
            s += A[j]
            win.add(A[j])
            ans = max(ans, s)
        return ans