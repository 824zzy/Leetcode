""" L2
insert x into arr and use two pointer to find K closest elements.
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = [-float('inf')] + arr + [float('inf')]
        idx = bisect.bisect(arr,x)
        i, j = idx-1, idx
        while 1:
            if abs(arr[i]-x)<=abs(arr[j]-x): i -= 1
            else: j += 1
            if j-i==k+1: return arr[i+1:j]