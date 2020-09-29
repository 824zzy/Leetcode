class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        cnt = Counter()
        prefix = 0
        ans = 0
        cnt[0] = 1
        for n in A:
            prefix += n
            ans += cnt[prefix-S]
            cnt[prefix] += 1
        return ans