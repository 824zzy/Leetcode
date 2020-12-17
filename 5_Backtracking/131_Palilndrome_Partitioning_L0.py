""" Back-tracking
"""
# old
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        
        def dfs(cur_s: str, temp: List[str]) -> None:
            if not cur_s:
                self.res.append(temp[:])
                return
            for i in range(1, len(cur_s)+1):
                if cur_s[:i] == cur_s[:i][::-1]:
                    dfs(cur_s[i:], temp+[cur_s[:i]])

        dfs(s, [])
        return self.res

# latest
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        def dfs(rm, path):
            if rm==rm[::-1]:
                self.ans.append(path+[rm])
            for i in range(1, len(rm)):
                if rm[:i]==rm[:i][::-1]:
                    dfs(rm[i:], path+[rm[:i]])
        dfs(s, [])
        return self.ans