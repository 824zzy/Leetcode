""" https://leetcode.com/problems/find-median-from-data-stream/
"""
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.L, num)
        
    def findMedian(self) -> float:
        if len(self.L)%2!=0: return self.L[len(self.L)//2] # odd
        else: return (self.L[len(self.L)//2]+self.L[len(self.L)//2-1])/2 # even