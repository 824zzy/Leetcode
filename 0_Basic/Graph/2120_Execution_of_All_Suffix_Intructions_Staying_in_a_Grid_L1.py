""" https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/
brute force
"""
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        for i in range(len(s)):
            x, y = startPos
            step = 0
            for j in range(i, len(s)):
                if s[j]=='L': y -= 1
                elif s[j]=='R': y += 1
                elif s[j]=='U': x -= 1
                else: x += 1
                
                if 0<=x<n and 0<=y<n: step += 1
                else: break
                
            ans.append(step)
        return ans
        