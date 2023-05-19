""" https://leetcode.com/problems/beautiful-arrangement/
1. backtracking
2. dfs with set
"""
# backtracking template
class Solution:
    def countArrangement(self, n: int) -> int:
        stk = []
        
        def dfs(i):
            if i==n+1:
                self.ans += 1
                return
            for x in range(1, n+1):
                if x not in stk and (x%i==0 or i%x==0):
                    stk.append(x)
                    dfs(i+1)
                    stk.pop()
        
        self.ans = 0
        dfs(1)
        return self.ans


# dfs with set
class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(A):
            if len(A)==n:
                self.ans += 1
                return
            for x in range(1, n+1):
                i = len(A)+1
                if x not in A and (x%i==0 or i%x==0):
                    A.add(x)
                    dfs(A)
                    A.remove(x)
        
        A = set()
        self.ans = 0
        dfs(A)
        return self.ans