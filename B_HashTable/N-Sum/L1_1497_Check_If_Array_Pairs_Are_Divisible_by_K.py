""" https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
1. use hash table to record the frequency of remainders x%target.
2. there will be only two cases:
    1. if k==0 (the original number is divisible by target), then we need to check if the frequency of remainders is even.
    2. if k!=0, then we need to check if the frequency of remainders is odd.
"""


class Solution:
    def canArrange(self, A: List[int], target: int) -> bool:
        cnt = Counter([x % target for x in A])
        for k, v in cnt.items():
            if k == 0:
                if v & 1:
                    return False
            elif cnt[target - k] != cnt[k]:
                return False
        return True
