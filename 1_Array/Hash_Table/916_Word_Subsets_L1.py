class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnts = Counter()
        for b in B: cnts = cnts|Counter(b) 
            
        ans = []
        for a in A:
            if Counter(a)|cnts==Counter(a): ans.append(a)
        return ans