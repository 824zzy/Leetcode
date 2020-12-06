class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans, s = [], [i for i in range(len(S)+1)]
        for c in S:
            if c=='I': ans.append(s.pop(0))
            else: ans.append(s.pop())
        ans.append(s.pop())
        return ans