""" https://leetcode.com/problems/recover-the-original-array/
greedily check every difference that is positive and even,
similar idea with 954, the pairs are not doubled but with constant difference.
"""
class Solution:
    def recoverArray(self, A: List[int]) -> List[int]:
        A.sort()
        for i in range(1, len(A)):
            diff = A[i]-A[0]
            if diff>0 and diff&1==0:
                ans = []
                freq = Counter(A)
                for k, v in freq.items():
                    if v:
                        if freq[k+diff]<v: break
                        ans.extend([k+diff//2]*v)
                        freq[k+diff] -= v
                else: return ans