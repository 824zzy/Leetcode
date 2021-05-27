""" L1: 

"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        q = defaultdict(int)
        for word in words:
            mask = 0
            for w in set(word):
                mask |= 1 << (ord(w)-ord('a'))
            q[mask] = max(q[mask], len(word))
            
        ans = 0
        for x in q:
            for y in q:
                if x == y: continue
                if not x & y:
                    ans = max(ans, q[x] * q[y])
        return ans
    
# straight-forward solution using set
class Solution:
    def maxProduct(self, W: List[str]) -> int:
        S = [set(w) for w in W]
        ans = 0
        for i in range(len(W)):
            for j in range(i+1, len(W)):
                if not S[i]&S[j]: 
                    ans = max(ans, len(W[i])*len(W[j]))
        return ans if ans else 0