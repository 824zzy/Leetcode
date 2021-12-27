from collections import Counter
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cnt = Counter()
        cnt[0] = 1
        res = 0
        prefix = 0
        for a in A:
            prefix = (prefix + a) % K
            res += cnt[prefix]
            cnt[prefix] += 1
        return res