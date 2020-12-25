class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            g = False
            for j in range(nums2.index(n), len(nums2)):
                if nums2[j]>n:
                    ans.append(nums2[j])
                    g = True
                    break
            if not g: ans.append(-1)
        return ans