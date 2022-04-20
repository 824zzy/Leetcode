""" https://leetcode.com/problems/sequential-digits/
greedily enumerate all possible answers from small to large
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l, r = len(str(low)), len(str(high))
        ans = []
        for i in range(l, r+1):
            for x in range(1, 10-i+1):
                n = int(''.join([str(d) for d in range(x, x+i)]))
                if low<=n<=high: 
                    ans.append(n)
        return ans
    
# neat solution from ye15
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for x in range(1, 10): 
            val = 0 
            for d in range(x, 10): 
                val = 10*val + d
                if low <= val <= high: ans.append(val)
        return sorted(ans)