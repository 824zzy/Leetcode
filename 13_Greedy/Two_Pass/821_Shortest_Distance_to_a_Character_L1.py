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
    
    
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [float('inf')] * len(S)
        cnt = float('inf')
        for i, s in enumerate(S):
            if s==C:
                cnt = 0
                ans[i] = 0
            else:
                cnt += 1
                ans[i] = min(ans[i], cnt)
        ans, cnt = ans[::-1], float('inf')
        for i, s in enumerate(S[::-1]):
            if s==C:
                cnt = 0
                ans[i] = 0
            else:
                cnt += 1
                ans[i] = min(ans[i], cnt)
        return ans[::-1]