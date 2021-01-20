class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter(nums)
        ans = 0
        for m, v in cnt.items():
            if k==2*m: 
                ans += v//2
                cnt[m] -= v
            elif k-m in cnt: 
                freq = min(v, cnt[k-m])
                cnt[m] -= freq
                cnt[k-m] -= freq
                ans += freq
        return ans