""" L2: https://leetcode.com/problems/additive-number/
TODO: https://leetcode.com/problems/additive-number/discuss/792460/python3-backtracking-similer-solution-for-842(Split-Array-into-Fibonacci-Sequence-)
used back tracking code same as #842(Split Array into Fibonacci Sequence )
"""
class Solution:
    def isAdditiveNumber(self, A: str) -> bool:
        self.stk = []
        def dfs(i):
            if i==len(A) and len(self.stk)>=3:  return True
            for j in range(i, len(A)):
                if A[i]=='0' and i!=j: break
                n = int(A[i:j+1])
                if len(self.stk)>=2 and self.stk[-2]+self.stk[-1]<n: break
                if len(self.stk)<=1 or self.stk[-2]+self.stk[-1]==n:
                    self.stk.append(n)
                    if dfs(j+1): return True
                    self.stk.pop()
            return False
        
        dfs(0)
        return len(self.stk)>0