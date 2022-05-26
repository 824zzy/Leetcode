""" L1: https://leetcode.com/problems/find-k-closest-elements/
find idx by bisect_left and use two pointers to find the k closest elements
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = [-float('inf')] + arr + [float('inf')]
        idx = bisect.bisect_left(arr,x)
        i, j = idx-1, idx
        while 1:
            if abs(arr[i]-x)<=abs(arr[j]-x): i -= 1
            else: j += 1
            if j-i==k+1: return arr[i+1:j]