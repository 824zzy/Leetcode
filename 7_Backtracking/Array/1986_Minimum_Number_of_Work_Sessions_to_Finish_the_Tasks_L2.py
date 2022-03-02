""" https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
from https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/discuss/1433054/Python-or-Backtracking-or-664ms-or-100-time-and-space-or-Explanation
"""
class Solution:
    def minSessions(self, A: List[int], T: int) -> int:
        A.sort(reverse=True) # pruning
        self.ans = len(A)
        stk = []
        
        def dfs(i):
            if len(stk)>=self.ans: return # pruning
            if i==len(A):
                self.ans = min(self.ans, len(stk))
                return
            for j in range(len(stk)):
                if stk[j]+A[i]<=T:
                    stk[j] += A[i]
                    dfs(i+1)
                    stk[j] -= A[i]
            stk.append(A[i])
            dfs(i+1)
            stk.pop()
        
        dfs(0)
        return self.ans
            
            