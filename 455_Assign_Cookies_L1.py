""" Basic greedy
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans, g, s = 0, sorted(g), sorted(s)
        
        while g and s:
            if g[-1] > s[-1]:
                g.pop()
            else:
                ans += 1
                g.pop()
                s.pop()
        
        return ans