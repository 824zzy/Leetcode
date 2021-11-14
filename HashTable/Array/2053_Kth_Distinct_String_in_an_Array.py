""" L1: https://leetcode.com/problems/kth-distinct-string-in-an-array/
find kth distinct string by counter
"""
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for x in arr: 
            if freq[x] == 1: k -= 1
            if k == 0: return x
        return ""

# TODO: remove this stupid solution
class Solution:
    def kthDistinct(self, A: List[str], k: int) -> str:
        cnt = defaultdict(list)
        for i, x in enumerate(A):
            if x in cnt: cnt[x][1] += 1
            else: cnt[x] = [i, 1]
                
        cnt = sorted([[k, v] for k, v in cnt.items() if v[1]==1], key=lambda x: x[1][0])
        if len(cnt)>=k: return cnt[k-1][0]
        else: return ""