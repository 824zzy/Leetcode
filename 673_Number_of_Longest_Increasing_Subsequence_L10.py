"""
"""
class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        n, MAX = len(nums), float("inf")
        ends = [[MAX, []] for _ in range(n)]
        for v in nums:
            i = bisect.bisect_left(ends, [v, []])
            cnt = sum(c for x, c in ends[i-1][1] if x < v) if i else 1
            ends[i][0] = v
            ends[i][1].append((v, cnt))
        return sum(c for v, c in next((cnts for mv, cnts in reversed(ends) if mv != MAX), []))





"""
"""
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp=[1]*len(nums)
        times=[1]*len(nums)
        res,max_len=1,1
        for i in xrange(1,len(nums)):
            for j in xrange(i):
                if nums[i]>nums[j]:
                    if 1+dp[j]>dp[i]:
                        dp[i]=1+dp[j]
                        times[i]=times[j]
                    elif 1+dp[j]==dp[i]:
                        times[i]+=times[j]
            if dp[i]>max_len:
                max_len=dp[i]
                res=times[i]
            elif dp[i]==max_len:
                res+=times[i]                
        return res




"""
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp1 = [1] * len(nums) # longest subsequence ending at index j
        for j in range(1, len(nums)):
            temp = []
            for i in range(j):
                if nums[i] < nums[j]:
                    temp.append(1+dp1[i])
            dp1[j] = max(temp or [1])
        
        dp2 = [0] * len(nums)
        for j in range(len(nums)):
            if dp1[j] == 1:
                dp2[j] = 1
            else:
                temp = []
                for i in range(j):
                    if nums[i] < nums[j] and dp1[i]+1 == dp1[j]:
                        temp.append(dp2[i])
                dp2[j] = sum(temp)
        m = max(dp1 or [0])
        
        ans = []
        for i in range(len(nums)):
            if dp1[i] == m:
                ans.append(dp2[i])
        return sum(ans or [0])