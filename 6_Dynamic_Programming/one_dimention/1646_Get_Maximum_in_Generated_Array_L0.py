class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(n+1):
            if 2*i<n+1:
                dp[2*i] = dp[i]
            if 2*i+1<n+1:
                dp[2*i+1] = dp[i]+dp[i+1]
        return max(dp)
    
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l=[0]*(n+1)
        if n==0:
            return 0
        l[1]=1
        for i in range(1,(n+1)//2):
            l[2*i]=l[i]
            l[2*i + 1]= l[i]+l[i+1]
        return max(l)