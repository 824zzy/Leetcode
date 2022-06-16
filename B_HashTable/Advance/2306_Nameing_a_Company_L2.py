""" https://leetcode.com/problems/naming-a-company/
from lee: https://leetcode.com/problems/naming-a-company/discuss/2141172/JavaC%2B%2BPython-Group-by-First-Letter

Any idea = first letter + postfix string.
We can group all ideas by their first letter.

If two ideas ideas[i] and ideas[j] share a common postfix string,
then ideas[i] can not pair with any idea starts with ideas[j][0]
and ideas[j] can not pair with any idea starts with ideas[i][0].

"""
class Solution:
    def distinctNames(self, A: List[str]) -> int:
        mp = defaultdict(set)
        for x in A: mp[x[0]].add(hash(x[1:]))
        
        ans = 0
        for a, seta in mp.items():
            for b, setb in mp.items():
                if a>=b: continue
                same = len(seta&setb)
                ans += (len(seta) - same) * (len(setb) - same)
        return ans*2 

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
            # Group strings by their initials
            A = [set() for _ in range(26)]
            for idea in ideas:
                A[ord(idea[0]) - ord('a')].add(idea[1:])
            
            ans = 0
            # Calculate number of valid names from every initial pair.
            for i in range(25):
                for j in range(i + 1, 26):
                    k = len(A[i] & A[j]) # Number of duplicated suffixes
                    ans += 2 * (len(A[i]) - k) * (len(A[j]) - k)
            return ans