""" https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/
problem conversion
find square as a hole ==> find consecutive bars ==> greedy
"""
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        
        def find_consecutive(A):
            A += [inf]
            i = 0
            ans = 0
            for j in range(1, len(A)):
                if A[j]!=A[j-1]+1:
                    i = j
                ans = max(ans, j-i+1)
            return ans
        
        a = find_consecutive(hBars)
        b = find_consecutive(vBars)
        return (min(a, b)+1)**2
    
"""
2
1
[2,3]
[2]
1
1
[2]
[2]
2
3
[2,3]
[2,3,4]
3
2
[3,2,4]
[3,2]
"""