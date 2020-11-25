class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [float('inf')] * len(S)
        pos = float('-inf')
        for i in range(len(S)):
            if S[i]==C:
                pos = i
            ans[i] = min(ans[i], abs(i-pos))
        for i in range(len(S))[::-1]:
            if S[i]==C:
                pos = i
            ans[i] = min(ans[i], abs(pos-i))
        return ans