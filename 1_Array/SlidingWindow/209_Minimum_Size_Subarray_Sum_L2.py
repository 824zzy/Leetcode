class Solution:
    def minSubArrayLen(self, s: int, A: List[int]) -> int:
        i, ans = 0, len(A)+1
        for j in range(len(A)):
            s -= A[j]
            while s<=0:
                ans = min(ans, j-i+1)
                s += A[i]
                i += 1
        return ans % (len(A)+1)