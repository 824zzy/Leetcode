""" https://leetcode.com/problems/minimize-deviation-in-array/
1. Convert all numbers to even. Then, we don't have to worry about 2nd operation entirely. 
2. Maintain a max heap and progressively divide the largest number by 2 until one cannot. The minimum deviation generation in this process is the required answer.
"""
from header import *

class Solution:
    def minimumDeviation(self, A: List[int]) -> int:
        A = [-2*x if x&1 else -x for x in A]
        heapify(A)
        ma = max(A)
        ans = ma-A[0]
        
        while A[0]&1==0:
            x = heappop(A)//2
            heappush(A, x)
            ma = max(ma, x)
            ans = min(ans, ma-A[0])
        return ans


# Alternative solution using SortedList
class Solution:
    def minimumDeviation(self, A: List[int]) -> int:
        A = [2*x if x&1 else x for x in A]
        sl = SortedList(A)
        ans = sl[-1]-sl[0]
        while sl[-1]&1==0:
            x = sl.pop()
            sl.add(x//2)
            ans = min(ans, sl[-1]-sl[0])
        return ans