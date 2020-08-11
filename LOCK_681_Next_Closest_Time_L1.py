"""
TODO:
"""

l = int(input())
candy = [int(c) for c in str(input()).split()]

dp = [0 for _ in range(l)]
dp[0] = candy[0]
dp[1] = candy[1]
dp[2] = max(candy[0]+candy[2], candy[2])
for i in range(3, l):
    dp[i] = max(candy[i]+dp[i-2], candy[i]+dp[i-3])
print(max(dp[-1], dp[-2], dp[-3]))