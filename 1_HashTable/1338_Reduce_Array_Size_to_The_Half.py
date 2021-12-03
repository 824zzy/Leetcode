""" L0
Use a sorted Counter as stack to reach threshold t
"""
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        t = len(arr)//2
        cnt = sorted(Counter(arr).items(), key=lambda x: -x[1])
        ans = 0
        while t>0: 
            t -= cnt.pop(0)[1]
            ans += 1
        return ans