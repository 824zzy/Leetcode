""" L3: https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
bfs+mask to find all sub puzzles.
"""
class Solution:
    def findNumOfValidWords(self, W: List[str], P: List[str]) -> List[int]:
        freq = Counter()
        for w in W:
            m = 0
            for c in w: m |= 1<<(ord(c)-97) 
            freq[m] += 1
        
        ans = []
        for p in P:
            bfs = [1<<(ord(p[0])-97)]
            for c in p[1:]:
                bfs += [m | 1<<(ord(c)-97) for m in bfs]
            ans.append(sum(freq[m] for m in bfs))
        
        return ans