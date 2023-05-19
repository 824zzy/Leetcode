class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = [0] * (len(nums)+1)
        for i in range(len(cnt)-1): cnt[nums[i]] += 1
        
        dup, miss = 0, 0
        for i in range(1, len(cnt)):
            if cnt[i]==2: dup = i
            if cnt[i]==0: miss = i
        return [dup, miss]