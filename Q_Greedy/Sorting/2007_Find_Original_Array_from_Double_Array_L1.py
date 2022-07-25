""" https://leetcode.com/problems/find-original-array-from-doubled-array/
1. greedily scan the sorted counter from small to large
2. update the larger element's frequency, be careful to corner case 0
"""
class Solution:
    def findOriginalArray(self, A: List[int]) -> List[int]:
        cnt = Counter(A)
        ans = []
        for k in sorted(cnt):
            if k==0:
                if cnt[k]%2: return []
                else: ans.extend([k]*(cnt[k]//2))
            else:
                if cnt[k]>cnt[2*k]: return []
                else:
                    cnt[2*k] -= cnt[k]
                    ans.extend([k]*cnt[k])
        return ans