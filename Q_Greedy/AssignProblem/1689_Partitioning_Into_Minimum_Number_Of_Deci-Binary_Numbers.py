""" Interesting brain teaser
"""
class Solution:
    def minPartitions(self, n: str) -> int:
        ans = int(n[0])
        ma = int(n[0])
        for i in range(1, len(n)):
            if int(n[i])>ma:
                ans += int(int(n[i])-ma)
                ma = int(n[i])
        return ans
    
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(x))