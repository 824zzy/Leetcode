""" L1: https://leetcode.com/problems/subsets-ii/
TODO: need to be optimized: https://leetcode.com/problems/subsets-ii/discuss/682110/Python3-recursive-and-iterative-solutions
"""
class Solution:
    def subsetsWithDup(self, A: List[int]) -> List[List[int]]:
        self.ans = []
        
        def dfs(P, N):
            if sorted(P) not in self.ans:
                self.ans.append(sorted(P))
            if not N: return
            for i, n in enumerate(N):
                dfs(P+[n], N[i+1:])
        
        dfs([], A)
        return self.ans