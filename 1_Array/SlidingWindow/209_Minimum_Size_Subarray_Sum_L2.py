class Solution:
    def minSubArrayLen(self, s: int, A: List[int]) -> int:
        i = 0
        ans = len(A)+1
        for j in range(len(A)):
            s -= A[j]
            while s<=0 and i<j:
                ans = min(j-i+1, ans)
                s += A[i]
                i += 1
        return ans % (len(A)+1)