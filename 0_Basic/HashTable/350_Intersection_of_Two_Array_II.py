""" L0: Find intersections by Counter since the order is not considered.
"""
class Solution:
    def intersect(self, A: List[int], B: List[int]) -> List[int]:
        cntA, cntB = Counter(A), Counter(B)
        ans = []
        for k, v in cntA.items():
            if k in cntB: ans.extend([k]*min(cntA[k], cntB[k])) 
        return ans
    
# another solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res += num
                counts[num] -= 1
        return res