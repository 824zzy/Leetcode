class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def dfs(p, l, r):
            if l==0 and r==0:
                self.ans.append(p)
            else:
                if l>0:
                    dfs(p+'(', l-1, r+1)
                if r>0:
                    dfs(p+')', l, r-1)
        dfs('', n, 0)
        return self.ans