# Naive backtracking
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        def dfs(path, curr, n, k):
            if k==0 and n==0:
                self.ans.append(path)
                return
            elif k<0 or n<0:
                return
            for i in range(curr+1, 10):
                dfs(path+[i], i, n-i, k-1)
        dfs([], 0, n, k)
        return self.ans

# itertools
from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [l for l in combinations(range(1, 10), k) if sum[l]==n]