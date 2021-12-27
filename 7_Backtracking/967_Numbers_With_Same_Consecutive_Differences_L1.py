""" Interesting problem
"""
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n==1: return [0,1,2,3,4,5,6,7,8,9]
        self.ans = set()
        def dfs(cur, n):
            if n==0: 
                self.ans.add(cur)
                return
            
            if 0<=int(cur[-1])+k<10: dfs(cur+str(int(cur[-1])+k), n-1)
            if int(cur[-1])-k>=0: dfs(cur+str((int(cur[-1])-k)), n-1)
        
        for i in [1,2,3,4,5,6,7,8,9]: dfs(str(i), n-1)
        return list(map(int, list(self.ans)))
