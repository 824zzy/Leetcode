class Solution:
    def findPoisonedDuration(self, s: List[int], d: int) -> int:
        ans = 0
        s += [float('inf')]
        for i in range(len(s)-1):
            ans += min(d, s[i+1]-s[i])
        return ans