class Solution:
    def findPoisonedDuration(self, A: List[int], d: int) -> int:
        if not A: return 0
        
        ans = 0
        for i in range(1, len(A)):
            ans += min(A[i]-A[i-1], d)
        return ans+d