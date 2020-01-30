class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        ans = 0
        j = 0
        for i in g:
            while j<len(s) and i>s[j]:
                j += 1
            if j<len(s):
                j += 1
                ans += 1
        return ans

        
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
    
