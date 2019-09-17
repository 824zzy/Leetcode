""" Binary Search
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ref_array = []
        self.length = 0
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # keep a sorted array
        # use binary search to find insertion index
        
        low = 0
        high = self.length - 1
        
        while low <= high:
            mid = (low+high)//2
            if self.ref_array[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1
                
        self.ref_array.insert(low,num)
        self.length += 1
            

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # as array is always sorted we can always use the same median property
        
        if self.length % 2 == 0:
            temp = self.length // 2
            return (self.ref_array[temp]+self.ref_array[temp-1])/2.0
        else:
            return self.ref_array[self.length // 2]


""" heapq & Binary Search
"""
from heapq import heappush, heappop, nsmallest, nlargest
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heappush(self.low, -num)
        # balancing step
        heappush(self.high, -heappop(self.low))
        
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low)>len(self.high):
            return -nsmallest(1, self.low)[0]
        else:
            return (-nsmallest(1, self.low)[0]+nsmallest(1, self.high)[0])/2
        

