""" https://leetcode.com/problems/find-unique-binary-string/
Find unique binary string by backtracking
"""
class Solution:
    def findDifferentBinaryString(self, A: List[str]) -> str:
        L = len(A[0])
        stk = []
        self.ans = ''
        
        def dfs(i):
            state = ''.join(stk)
            if i==L:
                if state not in A: 
                    self.ans = state
                    return True
                else: return False
            for c in ['0', '1']:
                stk.append(c)
                if dfs(i+1): return True
                stk.pop()
        
        dfs(0)
        return self.ans
    
class Solution:
    def findDifferentBinaryString(self, A: List[str]) -> str:
        self.ans = ""
        self.f = True
        def dfs(P):
            if len(P)==len(A[0]) and P not in A:
                self.ans, self.f = P, False
                return
            for i in ['0', '1']:
                if len(P)<len(A[0]) and self.f: dfs(P+i)
    
        dfs("")
        return self.ans
