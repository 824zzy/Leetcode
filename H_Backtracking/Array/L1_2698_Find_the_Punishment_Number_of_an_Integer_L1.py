""" https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
1 <= n <= 1000, brute force using backtracking

Time complexity: O(n^3)
"""

A = [0] * 1001
for x in range(1, 1001):
    S = str(x*x)
    n = len(S)
    sm = [0]
    def dfs(i):
        if i==n:
            return sm[0]==x
        s = 0
        for j in range(i, n):
            s = s*10+int(S[j])
            sm[0] += s
            if dfs(j+1):
                return True
            sm[0] -= s
        return False
    A[x] = dfs(0)
    

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for x in range(1, n+1):
            if A[x]:
                ans += x*x
        return ans
            
        
"""
1,234
12,34
123,4
"""