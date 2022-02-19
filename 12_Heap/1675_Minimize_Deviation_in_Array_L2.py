""" https://leetcode.com/problems/minimize-deviation-in-array/
from ye15: https://leetcode.com/problems/minimize-deviation-in-array/discuss/954165/Python3-priority-queue
Convert all numbers to even. Then, we don't have to worry about 2nd operation entirely. 
Maintain a max heap and progressively divide the largest number by 2 until one cannot. The minimum deviation generation in this process is the required answer.
"""
class Solution:
    def minimumDeviation(self, A: List[int]) -> int:
        A = [-2*x if x&1 else -x for x in A]
        heapq.heapify(A)
        ma = max(A)
        ans = ma-A[0]
        
        while A[0]&1==0:
            x = heapq.heappop(A)//2
            heappush(A, x)
            ma = max(ma, x)
            ans = min(ans, ma-A[0])
        return ans