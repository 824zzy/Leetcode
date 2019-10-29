class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1
        return res