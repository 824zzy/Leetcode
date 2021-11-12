""" Straight forward solution, low efficiency
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr)-1:
            if arr[i] == 0:
                arr[i:] == [0] + arr[i:-1]
                i += 2
            else:
                i += 1

""" Very tricky solution
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j, l = arr.count(0), len(arr)
        
        for i in reversed(range(len(arr))):
            if not arr[i]:
                j -= 1
                if i+j+1 < l:
                    arr[i+j+1] = 0
            if i+j < l:
                arr[i+j] = arr[i]                    
        