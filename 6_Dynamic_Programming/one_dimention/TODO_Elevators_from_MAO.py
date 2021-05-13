class Solution:
    def elevators(self, starts, heights, target):
        if target>max(heights): return -1
        dp = [float('inf')] * (max(heights)-min(starts)+1)
        dp[0] = 0
        for i, j in zip(starts, heights):
            if i>=0:
                for k in range(i+1, j+1):
                    dp[k] = min(dp[k], dp[i]+1)
            else:
                for k in range(j-1, i, -1):
                    # print(j, i, k)
                    dp[k] = min(dp[k], dp[j]+1)
                
                
        if dp[target]: return dp[target]
        else: return -1

if __name__ == '__main__':
    S = Solution()
    ans = S.elevators([0, 1], [1, 5], 4)
    print(ans)
    ans = S.elevators([0, 7, -10, -5, -3], [100, 3, 6, 4, 4], -4)
    print(ans)