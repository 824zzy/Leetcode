class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cnt = Counter()
        cnt[0] = -1
        prefix = 0
        ans = 0
        for i, n in enumerate(nums):
            if k:
                prefix = (prefix+n)%abs(k)
            else:
                prefix = (prefix+n)
                
            if prefix not in cnt:
                cnt[prefix] = i
            if i-cnt[prefix]>1:
                print(cnt)
                return True
        return False
