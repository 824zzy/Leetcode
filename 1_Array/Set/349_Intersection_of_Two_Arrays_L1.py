# set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = list(set(nums1)), set(nums2)
        ans = []
        for n in n1:
            if n in n2:
                ans.append(n)
        return ans


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans