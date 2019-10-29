class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            l, h, comp = 0, len(nums)-1, nums[-1]
            while l<=h:
                m = (l+h)//2
                if comp<nums[m]:
                    l = m + 1
                else:
                    h = m - 1
            return m
        
        def binSearch(low, high):
            l, h = low, high
            while l<=h:
                m = (l+h)//2
                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    h = m - 1
                else:
                    l = m + 1
            return -1
        
        if not nums:
            return -1
        pivot = findPivot()
        ans = binSearch(0, pivot)
        if ans!=-1:
            return ans
        else:
            return binSearch(pivot, len(nums)-1)