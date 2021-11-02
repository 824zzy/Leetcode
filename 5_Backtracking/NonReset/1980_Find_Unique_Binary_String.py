""" L0: https://leetcode.com/problems/find-unique-binary-string/
Find unique binary string by backtracking
"""
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
