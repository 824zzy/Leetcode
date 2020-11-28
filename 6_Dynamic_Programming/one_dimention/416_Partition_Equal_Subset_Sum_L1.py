class Solution:
    def canPartition(self, A: List[int]) -> bool:
        if sum(A)%2 != 0:
            return False
        dp = [0]*(sum(A)+1)
        dp[0] = 1
        for n in A:
            for i in range(int(sum(A)/2), -1, -1):
                if dp[i]: dp[i+n] = 1
            if dp[sum(A)//2]: return True
        return False