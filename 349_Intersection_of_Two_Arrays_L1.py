""" my basic solution using set
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n1 in nums1:
            if n1 in nums2:
                res.append(n1)
        return list(set(res))


""" better solution: the idea is the sam
time complexity saving pretty much in `if n1 in nums2:` and `if n in s1:`
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        s1 = set(nums1)
        intersec = []
        for n in nums2:
            if n in s1:
                intersec.append(n)
        intersec = set(intersec)
        
        return list(intersec)