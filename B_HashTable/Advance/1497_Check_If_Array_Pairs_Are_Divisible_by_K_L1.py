""" https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/discuss/709252/Python3-3-line-frequency-table
Define a frequency table freq to record the occurrence of numbers in arr in terms of its remainder x%k.
"""
class Solution:
    def canArrange(self, A: List[int], t: int) -> bool:
        cnt = Counter(x%t for x in A)
        for k, v in cnt.items():
            if k==(t-k)%t and cnt[k]%2!=0: return False
            elif cnt[k]!=cnt[(t-k)%t]:  return False
        return True